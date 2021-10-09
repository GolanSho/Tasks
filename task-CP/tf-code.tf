terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

provider "aws" {
    region  =   "us-east-1"
    shared_credentials_file = "$HOME/.aws/credentials"
    profile =   "golan"
}

resource "aws_vpc" "vpc" {
  cidr_block           = "172.24.24.0/24"
  enable_dns_hostnames = true

  tags = {
    Name = "test-vpc"
  }
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.vpc.id
  depends_on      = [aws_vpc.vpc]
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "test_public_route"
  }
  depends_on      = [aws_vpc.vpc, aws_internet_gateway.igw]
}

resource "aws_subnet" "public" {
  count			  = "2"
  vpc_id                  = aws_vpc.vpc.id
  cidr_block              = cidrsubnet(aws_vpc.vpc.cidr_block, 2, count.index)
  map_public_ip_on_launch = true

  tags = {
  Name = "test-public-${cidrsubnet(aws_vpc.vpc.cidr_block, 2, count.index)}"

    pub_priv = "public"
  }
  depends_on      = [aws_vpc.vpc]
}

resource "aws_lb" "nlb" {
  name               = "test-nlb"
  internal           = false
  load_balancer_type = "network"
  subnets            = aws_subnet.public.*.id

  enable_deletion_protection = true

  tags = {
    Environment = "test"
  }
  depends_on      = [aws_subnet.public]
}

resource "aws_lb_target_group" "svc-tg" {
  name     = "test-lb-tg"
  port     = 5000
  protocol = "TCP"
  vpc_id   = aws_vpc.vpc.id
  depends_on      = [aws_vpc.vpc]
}

resource "aws_lb_listener" "nlb-service" {
  load_balancer_arn = aws_lb.nlb.arn
  port              = 5000
  protocol          = "TCP"
  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.svc-tg.arn
  }
  depends_on      = [aws_lb.nlb, aws_lb_target_group.svc-tg]
}

resource "aws_ecs_cluster" "cluster" {
  name               = "test-cluster"
  setting {
    name  = "containerInsights"
    value = "enabled"
  }
}

resource "aws_ecr_repository" "image" {
  name                 = "count-app"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}

resource "aws_ecs_task_definition" "task" {
  family = "count-app"
  container_definitions = jsonencode([
    {
      name      = "count-app"
      image     = "${aws_ecr_repository.image.repository_url}:0.1"
      cpu       = 10
      memory    = 512
      essential = true
      portMappings = [
        {
          containerPort = 5000
          hostPort      = 5000
        }
      ]
    }
  ])
  depends_on      = [aws_ecr_repository.image]
}

resource "aws_launch_template" "ecs" {

  name = "ECS-test-LT"

  image_id = "ami-0ff8a91507f77f867"
  instance_initiated_shutdown_behavior = "terminate"
  instance_type = "t2.micro"
  ebs_optimized = false

  user_data = base64encode("echo ECS_CLUSTER='test-cluster' > /etc/ecs/ecs.config")

}

resource "aws_autoscaling_group" "ecs-cluster" {
    name                 = "ECS-test-ASG"
    min_size             ="1"
    max_size             = "2"
    desired_capacity     = "1"
    health_check_type    = "EC2"
                launch_template                  {
                        id = aws_launch_template.ecs.id
                        version = "$Latest"
                }
    vpc_zone_identifier  = [aws_subnet.public[0].id]
    tag{
        key = "Name"
        value = "ECS-test-Instance"
        propagate_at_launch = true
    }
  depends_on      = [aws_launch_template.ecs]
}

resource "aws_ecs_capacity_provider" "ec2_provider" {
  name = "test-provider"
  auto_scaling_group_provider {
    auto_scaling_group_arn         = aws_autoscaling_group.ecs-cluster.arn
    managed_termination_protection = "DISABLED"

    managed_scaling {
      maximum_scaling_step_size = 2
      minimum_scaling_step_size = 1
      status                    = "ENABLED"
      target_capacity           = 1
    }
  }
  depends_on      = [aws_autoscaling_group.ecs-cluster]
}

resource "aws_ecs_service" "service" {
  name            = "count-app"
  cluster         = aws_ecs_cluster.cluster.id
  task_definition = aws_ecs_task_definition.task.arn
  desired_count   = 1
  load_balancer {
    target_group_arn = aws_lb_target_group.svc-tg.arn
    container_name   = "count-app"
    container_port   = 5000
  }
  depends_on      = [aws_ecs_cluster.cluster, aws_ecs_task_definition.task, aws_lb_target_group.svc-tg, aws_lb.nlb]
}
