Name:           aws-sdk-cpp
Version:    1.0.62
Release:        1%{?dist}
Summary:    aws-sdk-cpp 
Group:      Applications/Engineering
License:    Apache License Version 2.0        
URL:        https://github.com/aws/aws-sdk-cpp
Source:     https://github.com/aws/aws-sdk-cpp/archive/%{version}.tar.gz

BuildRequires: cmake3 
BuildRequires: gcc-c++
BuildRequires: openssl-devel
BuildRequires: curl-devel
BuildRequires: libuuid-devel

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
C++ SDK for amazon web services


%prep
%setup -q

%build
mkdir -p build
pushd build
cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix}
make -j8
popd

%install
pushd build
make install DESTDIR=%{buildroot}
#if [ -d %{buildroot}/usr/lib ] ; then
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
#fi

popd

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%package access-management
Summary:        AWS access-management library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description access-management
Libraries for access-management

%package access-management-devel
Summary:        AWS access-management
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description access-management-devel
developement package for access-management

%package acm
Summary:        AWS acm library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description acm
Libraries for acm

%package acm-devel
Summary:        AWS acm
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description acm-devel
developement package for acm

%package apigateway
Summary:        AWS apigateway library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description apigateway
Libraries for apigateway

%package apigateway-devel
Summary:        AWS apigateway
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description apigateway-devel
developement package for apigateway

%package application-autoscaling
Summary:        AWS application-autoscaling library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description application-autoscaling
Libraries for application-autoscaling

%package application-autoscaling-devel
Summary:        AWS application-autoscaling
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description application-autoscaling-devel
developement package for application-autoscaling

%package appstream
Summary:        AWS appstream library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description appstream
Libraries for appstream

%package appstream-devel
Summary:        AWS appstream
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description appstream-devel
developement package for appstream

%package autoscaling
Summary:        AWS autoscaling library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description autoscaling
Libraries for autoscaling

%package autoscaling-devel
Summary:        AWS autoscaling
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description autoscaling-devel
developement package for autoscaling

%package budgets
Summary:        AWS budgets library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description budgets
Libraries for budgets

%package budgets-devel
Summary:        AWS budgets
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description budgets-devel
developement package for budgets

%package clouddirectory
Summary:        AWS clouddirectory library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description clouddirectory
Libraries for clouddirectory

%package clouddirectory-devel
Summary:        AWS clouddirectory
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description clouddirectory-devel
developement package for clouddirectory

%package cloudformation
Summary:        AWS cloudformation library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description cloudformation
Libraries for cloudformation

%package cloudformation-devel
Summary:        AWS cloudformation
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description cloudformation-devel
developement package for cloudformation

%package cloudfront
Summary:        AWS cloudfront library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description cloudfront
Libraries for cloudfront

%package cloudfront-devel
Summary:        AWS cloudfront
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description cloudfront-devel
developement package for cloudfront

%package cloudhsm
Summary:        AWS cloudhsm library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description cloudhsm
Libraries for cloudhsm

%package cloudhsm-devel
Summary:        AWS cloudhsm
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description cloudhsm-devel
developement package for cloudhsm

%package cloudsearchdomain
Summary:        AWS cloudsearchdomain library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description cloudsearchdomain
Libraries for cloudsearchdomain

%package cloudsearchdomain-devel
Summary:        AWS cloudsearchdomain
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description cloudsearchdomain-devel
developement package for cloudsearchdomain

%package cloudsearch
Summary:        AWS cloudsearch library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description cloudsearch
Libraries for cloudsearch

%package cloudsearch-devel
Summary:        AWS cloudsearch
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description cloudsearch-devel
developement package for cloudsearch

%package cloudtrail
Summary:        AWS cloudtrail library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description cloudtrail
Libraries for cloudtrail

%package cloudtrail-devel
Summary:        AWS cloudtrail
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description cloudtrail-devel
developement package for cloudtrail

%package codebuild
Summary:        AWS codebuild library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description codebuild
Libraries for codebuild

%package codebuild-devel
Summary:        AWS codebuild
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description codebuild-devel
developement package for codebuild

%package codecommit
Summary:        AWS codecommit library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description codecommit
Libraries for codecommit

%package codecommit-devel
Summary:        AWS codecommit
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description codecommit-devel
developement package for codecommit

%package codedeploy
Summary:        AWS codedeploy library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description codedeploy
Libraries for codedeploy

%package codedeploy-devel
Summary:        AWS codedeploy
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description codedeploy-devel
developement package for codedeploy

%package codepipeline
Summary:        AWS codepipeline library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description codepipeline
Libraries for codepipeline

%package codepipeline-devel
Summary:        AWS codepipeline
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description codepipeline-devel
developement package for codepipeline

%package cognito-identity
Summary:        AWS cognito-identity library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description cognito-identity
Libraries for cognito-identity

%package cognito-identity-devel
Summary:        AWS cognito-identity
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description cognito-identity-devel
developement package for cognito-identity

%package cognito-idp
Summary:        AWS cognito-idp library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description cognito-idp
Libraries for cognito-idp

%package cognito-idp-devel
Summary:        AWS cognito-idp
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description cognito-idp-devel
developement package for cognito-idp

%package cognito-sync
Summary:        AWS cognito-sync library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description cognito-sync
Libraries for cognito-sync

%package cognito-sync-devel
Summary:        AWS cognito-sync
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description cognito-sync-devel
developement package for cognito-sync

%package config
Summary:        AWS config library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description config
Libraries for config

%package config-devel
Summary:        AWS config
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description config-devel
developement package for config

%package core
Summary:        AWS core library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description core
Libraries for core

%package core-devel
Summary:        AWS core
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description core-devel
developement package for core

%package cur
Summary:        AWS cur library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description cur
Libraries for cur

%package cur-devel
Summary:        AWS cur
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description cur-devel
developement package for cur

%package datapipeline
Summary:        AWS datapipeline library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description datapipeline
Libraries for datapipeline

%package datapipeline-devel
Summary:        AWS datapipeline
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description datapipeline-devel
developement package for datapipeline

%package devicefarm
Summary:        AWS devicefarm library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devicefarm
Libraries for devicefarm

%package devicefarm-devel
Summary:        AWS devicefarm
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devicefarm-devel
developement package for devicefarm

%package directconnect
Summary:        AWS directconnect library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description directconnect
Libraries for directconnect

%package directconnect-devel
Summary:        AWS directconnect
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description directconnect-devel
developement package for directconnect

%package dms
Summary:        AWS dms library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description dms
Libraries for dms

%package dms-devel
Summary:        AWS dms
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description dms-devel
developement package for dms

%package ds
Summary:        AWS ds library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description ds
Libraries for ds

%package ds-devel
Summary:        AWS ds
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description ds-devel
developement package for ds

%package dynamodb
Summary:        AWS dynamodb library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description dynamodb
Libraries for dynamodb

%package dynamodb-devel
Summary:        AWS dynamodb
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description dynamodb-devel
developement package for dynamodb

%package ec2
Summary:        AWS ec2 library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description ec2
Libraries for ec2

%package ec2-devel
Summary:        AWS ec2
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description ec2-devel
developement package for ec2

%package ecr
Summary:        AWS ecr library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description ecr
Libraries for ecr

%package ecr-devel
Summary:        AWS ecr
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description ecr-devel
developement package for ecr

%package ecs
Summary:        AWS ecs library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description ecs
Libraries for ecs

%package ecs-devel
Summary:        AWS ecs
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description ecs-devel
developement package for ecs

%package elasticache
Summary:        AWS elasticache library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description elasticache
Libraries for elasticache

%package elasticache-devel
Summary:        AWS elasticache
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description elasticache-devel
developement package for elasticache

%package elasticbeanstalk
Summary:        AWS elasticbeanstalk library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description elasticbeanstalk
Libraries for elasticbeanstalk

%package elasticbeanstalk-devel
Summary:        AWS elasticbeanstalk
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description elasticbeanstalk-devel
developement package for elasticbeanstalk

%package elasticfilesystem
Summary:        AWS elasticfilesystem library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description elasticfilesystem
Libraries for elasticfilesystem

%package elasticfilesystem-devel
Summary:        AWS elasticfilesystem
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description elasticfilesystem-devel
developement package for elasticfilesystem

%package elasticloadbalancing
Summary:        AWS elasticloadbalancing library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description elasticloadbalancing
Libraries for elasticloadbalancing

%package elasticloadbalancing-devel
Summary:        AWS elasticloadbalancing
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description elasticloadbalancing-devel
developement package for elasticloadbalancing

%package elasticloadbalancingv2
Summary:        AWS elasticloadbalancingv2 library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description elasticloadbalancingv2
Libraries for elasticloadbalancingv2

%package elasticloadbalancingv2-devel
Summary:        AWS elasticloadbalancingv2
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description elasticloadbalancingv2-devel
developement package for elasticloadbalancingv2

%package elasticmapreduce
Summary:        AWS elasticmapreduce library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description elasticmapreduce
Libraries for elasticmapreduce

%package elasticmapreduce-devel
Summary:        AWS elasticmapreduce
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description elasticmapreduce-devel
developement package for elasticmapreduce

%package elastictranscoder
Summary:        AWS elastictranscoder library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description elastictranscoder
Libraries for elastictranscoder

%package elastictranscoder-devel
Summary:        AWS elastictranscoder
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description elastictranscoder-devel
developement package for elastictranscoder

%package email
Summary:        AWS email library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description email
Libraries for email

%package email-devel
Summary:        AWS email
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description email-devel
developement package for email

%package es
Summary:        AWS es library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description es
Libraries for es

%package es-devel
Summary:        AWS es
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description es-devel
developement package for es

%package events
Summary:        AWS events library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description events
Libraries for events

%package events-devel
Summary:        AWS events
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description events-devel
developement package for events

%package firehose
Summary:        AWS firehose library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description firehose
Libraries for firehose

%package firehose-devel
Summary:        AWS firehose
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description firehose-devel
developement package for firehose

%package gamelift
Summary:        AWS gamelift library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description gamelift
Libraries for gamelift

%package gamelift-devel
Summary:        AWS gamelift
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description gamelift-devel
developement package for gamelift

%package glacier
Summary:        AWS glacier library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description glacier
Libraries for glacier

%package glacier-devel
Summary:        AWS glacier
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description glacier-devel
developement package for glacier

%package health
Summary:        AWS health library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description health
Libraries for health

%package health-devel
Summary:        AWS health
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description health-devel
developement package for health

%package iam
Summary:        AWS iam library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description iam
Libraries for iam

%package iam-devel
Summary:        AWS iam
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description iam-devel
developement package for iam

%package identity-management
Summary:        AWS identity-management library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description identity-management
Libraries for identity-management

%package identity-management-devel
Summary:        AWS identity-management
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description identity-management-devel
developement package for identity-management

%package importexport
Summary:        AWS importexport library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description importexport
Libraries for importexport

%package importexport-devel
Summary:        AWS importexport
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description importexport-devel
developement package for importexport

%package inspector
Summary:        AWS inspector library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description inspector
Libraries for inspector

%package inspector-devel
Summary:        AWS inspector
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description inspector-devel
developement package for inspector

%package iot
Summary:        AWS iot library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description iot
Libraries for iot

%package iot-devel
Summary:        AWS iot
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description iot-devel
developement package for iot

%package kinesisanalytics
Summary:        AWS kinesisanalytics library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description kinesisanalytics
Libraries for kinesisanalytics

%package kinesisanalytics-devel
Summary:        AWS kinesisanalytics
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description kinesisanalytics-devel
developement package for kinesisanalytics

%package kinesis
Summary:        AWS kinesis library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description kinesis
Libraries for kinesis

%package kinesis-devel
Summary:        AWS kinesis
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description kinesis-devel
developement package for kinesis

%package kms
Summary:        AWS kms library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description kms
Libraries for kms

%package kms-devel
Summary:        AWS kms
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description kms-devel
developement package for kms

%package lambda
Summary:        AWS lambda library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description lambda
Libraries for lambda

%package lambda-devel
Summary:        AWS lambda
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description lambda-devel
developement package for lambda

%package lightsail
Summary:        AWS lightsail library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description lightsail
Libraries for lightsail

%package lightsail-devel
Summary:        AWS lightsail
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description lightsail-devel
developement package for lightsail

%package logs
Summary:        AWS logs library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description logs
Libraries for logs

%package logs-devel
Summary:        AWS logs
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description logs-devel
developement package for logs

%package machinelearning
Summary:        AWS machinelearning library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description machinelearning
Libraries for machinelearning

%package machinelearning-devel
Summary:        AWS machinelearning
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description machinelearning-devel
developement package for machinelearning

%package marketplacecommerceanalytics
Summary:        AWS marketplacecommerceanalytics library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description marketplacecommerceanalytics
Libraries for marketplacecommerceanalytics

%package marketplacecommerceanalytics-devel
Summary:        AWS marketplacecommerceanalytics
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description marketplacecommerceanalytics-devel
developement package for marketplacecommerceanalytics

%package meteringmarketplace
Summary:        AWS meteringmarketplace library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description meteringmarketplace
Libraries for meteringmarketplace

%package meteringmarketplace-devel
Summary:        AWS meteringmarketplace
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description meteringmarketplace-devel
developement package for meteringmarketplace

%package mobileanalytics
Summary:        AWS mobileanalytics library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description mobileanalytics
Libraries for mobileanalytics

%package mobileanalytics-devel
Summary:        AWS mobileanalytics
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description mobileanalytics-devel
developement package for mobileanalytics

%package monitoring
Summary:        AWS monitoring library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description monitoring
Libraries for monitoring

%package monitoring-devel
Summary:        AWS monitoring
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description monitoring-devel
developement package for monitoring

%package opsworkscm
Summary:        AWS opsworkscm library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description opsworkscm
Libraries for opsworkscm

%package opsworkscm-devel
Summary:        AWS opsworkscm
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description opsworkscm-devel
developement package for opsworkscm

%package opsworks
Summary:        AWS opsworks library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description opsworks
Libraries for opsworks

%package opsworks-devel
Summary:        AWS opsworks
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description opsworks-devel
developement package for opsworks

%package polly
Summary:        AWS polly library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description polly
Libraries for polly

%package polly-devel
Summary:        AWS polly
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description polly-devel
developement package for polly

%package queues
Summary:        AWS queues library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description queues
Libraries for queues

%package queues-devel
Summary:        AWS queues
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description queues-devel
developement package for queues

%package rds
Summary:        AWS rds library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description rds
Libraries for rds

%package rds-devel
Summary:        AWS rds
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description rds-devel
developement package for rds

%package redshift
Summary:        AWS redshift library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description redshift
Libraries for redshift

%package redshift-devel
Summary:        AWS redshift
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description redshift-devel
developement package for redshift

%package rekognition
Summary:        AWS rekognition library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description rekognition
Libraries for rekognition

%package rekognition-devel
Summary:        AWS rekognition
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description rekognition-devel
developement package for rekognition

%package route53domains
Summary:        AWS route53domains library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description route53domains
Libraries for route53domains

%package route53domains-devel
Summary:        AWS route53domains
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description route53domains-devel
developement package for route53domains

%package route53
Summary:        AWS route53 library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description route53
Libraries for route53

%package route53-devel
Summary:        AWS route53
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description route53-devel
developement package for route53

%package s3-encryption
Summary:        AWS s3-encryption library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description s3-encryption
Libraries for s3-encryption

%package s3-encryption-devel
Summary:        AWS s3-encryption
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description s3-encryption-devel
developement package for s3-encryption

%package s3
Summary:        AWS s3 library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description s3
Libraries for s3

%package s3-devel
Summary:        AWS s3
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description s3-devel
developement package for s3

%package sdb
Summary:        AWS sdb library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description sdb
Libraries for sdb

%package sdb-devel
Summary:        AWS sdb
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description sdb-devel
developement package for sdb

%package servicecatalog
Summary:        AWS servicecatalog library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description servicecatalog
Libraries for servicecatalog

%package servicecatalog-devel
Summary:        AWS servicecatalog
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description servicecatalog-devel
developement package for servicecatalog

%package shield
Summary:        AWS shield library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description shield
Libraries for shield

%package shield-devel
Summary:        AWS shield
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description shield-devel
developement package for shield

%package snowball
Summary:        AWS snowball library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description snowball
Libraries for snowball

%package snowball-devel
Summary:        AWS snowball
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description snowball-devel
developement package for snowball

%package sns
Summary:        AWS sns library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description sns
Libraries for sns

%package sns-devel
Summary:        AWS sns
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description sns-devel
developement package for sns

%package sqs
Summary:        AWS sqs library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description sqs
Libraries for sqs

%package sqs-devel
Summary:        AWS sqs
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description sqs-devel
developement package for sqs

%package ssm
Summary:        AWS ssm library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description ssm
Libraries for ssm

%package ssm-devel
Summary:        AWS ssm
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description ssm-devel
developement package for ssm

%package states
Summary:        AWS states library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description states
Libraries for states

%package states-devel
Summary:        AWS states
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description states-devel
developement package for states

%package storagegateway
Summary:        AWS storagegateway library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description storagegateway
Libraries for storagegateway

%package storagegateway-devel
Summary:        AWS storagegateway
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description storagegateway-devel
developement package for storagegateway

%package sts
Summary:        AWS sts library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description sts
Libraries for sts

%package sts-devel
Summary:        AWS sts
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description sts-devel
developement package for sts

%package support
Summary:        AWS support library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description support
Libraries for support

%package support-devel
Summary:        AWS support
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description support-devel
developement package for support

%package swf
Summary:        AWS swf library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description swf
Libraries for swf

%package swf-devel
Summary:        AWS swf
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description swf-devel
developement package for swf

%package transfer
Summary:        AWS transfer library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description transfer
Libraries for transfer

%package transfer-devel
Summary:        AWS transfer
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description transfer-devel
developement package for transfer

%package waf
Summary:        AWS waf library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description waf
Libraries for waf

%package waf-devel
Summary:        AWS waf
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description waf-devel
developement package for waf

%package workspaces
Summary:        AWS workspaces library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description workspaces
Libraries for workspaces

%package workspaces-devel
Summary:        AWS workspaces
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description workspaces-devel
developement package for workspaces

%package xray
Summary:        AWS xray library
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description xray
Libraries for xray

%package xray-devel
Summary:        AWS xray
Group:          System Environment/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description xray-devel
developement package for xray

%files access-management
%{_libdir}/lib*access-management.so

%files access-management-devel
%{_includedir}/aws/access-management

%files acm
%{_libdir}/lib*acm.so

%files acm-devel
%{_includedir}/aws/acm

%files apigateway
%{_libdir}/lib*apigateway.so

%files apigateway-devel
%{_includedir}/aws/apigateway

%files application-autoscaling
%{_libdir}/lib*application-autoscaling.so

%files application-autoscaling-devel
%{_includedir}/aws/application-autoscaling

%files appstream
%{_libdir}/lib*appstream.so

%files appstream-devel
%{_includedir}/aws/appstream

%files autoscaling
%{_libdir}/lib*autoscaling.so

%files autoscaling-devel
%{_includedir}/aws/autoscaling

%files budgets
%{_libdir}/lib*budgets.so

%files budgets-devel
%{_includedir}/aws/budgets

%files clouddirectory
%{_libdir}/lib*clouddirectory.so

%files clouddirectory-devel
%{_includedir}/aws/clouddirectory

%files cloudformation
%{_libdir}/lib*cloudformation.so

%files cloudformation-devel
%{_includedir}/aws/cloudformation

%files cloudfront
%{_libdir}/lib*cloudfront.so

%files cloudfront-devel
%{_includedir}/aws/cloudfront

%files cloudhsm
%{_libdir}/lib*cloudhsm.so

%files cloudhsm-devel
%{_includedir}/aws/cloudhsm

%files cloudsearchdomain
%{_libdir}/lib*cloudsearchdomain.so

%files cloudsearchdomain-devel
%{_includedir}/aws/cloudsearchdomain

%files cloudsearch
%{_libdir}/lib*cloudsearch.so

%files cloudsearch-devel
%{_includedir}/aws/cloudsearch

%files cloudtrail
%{_libdir}/lib*cloudtrail.so

%files cloudtrail-devel
%{_includedir}/aws/cloudtrail

%files codebuild
%{_libdir}/lib*codebuild.so

%files codebuild-devel
%{_includedir}/aws/codebuild

%files codecommit
%{_libdir}/lib*codecommit.so

%files codecommit-devel
%{_includedir}/aws/codecommit

%files codedeploy
%{_libdir}/lib*codedeploy.so

%files codedeploy-devel
%{_includedir}/aws/codedeploy

%files codepipeline
%{_libdir}/lib*codepipeline.so

%files codepipeline-devel
%{_includedir}/aws/codepipeline

%files cognito-identity
%{_libdir}/lib*cognito-identity.so

%files cognito-identity-devel
%{_includedir}/aws/cognito-identity

%files cognito-idp
%{_libdir}/lib*cognito-idp.so

%files cognito-idp-devel
%{_includedir}/aws/cognito-idp

%files cognito-sync
%{_libdir}/lib*cognito-sync.so

%files cognito-sync-devel
%{_includedir}/aws/cognito-sync

%files config
%{_libdir}/lib*config.so

%files config-devel
%{_includedir}/aws/config

%files core
%{_libdir}/lib*core.so

%files core-devel
%{_includedir}/aws/core

%files cur
%{_libdir}/lib*cur.so

%files cur-devel
%{_includedir}/aws/cur

%files datapipeline
%{_libdir}/lib*datapipeline.so

%files datapipeline-devel
%{_includedir}/aws/datapipeline

%files devicefarm
%{_libdir}/lib*devicefarm.so

%files devicefarm-devel
%{_includedir}/aws/devicefarm

%files directconnect
%{_libdir}/lib*directconnect.so

%files directconnect-devel
%{_includedir}/aws/directconnect

%files dms
%{_libdir}/lib*dms.so

%files dms-devel
%{_includedir}/aws/dms

%files ds
%{_libdir}/lib*ds.so

%files ds-devel
%{_includedir}/aws/ds

%files dynamodb
%{_libdir}/lib*dynamodb.so

%files dynamodb-devel
%{_includedir}/aws/dynamodb

%files ec2
%{_libdir}/lib*ec2.so

%files ec2-devel
%{_includedir}/aws/ec2

%files ecr
%{_libdir}/lib*ecr.so

%files ecr-devel
%{_includedir}/aws/ecr

%files ecs
%{_libdir}/lib*ecs.so

%files ecs-devel
%{_includedir}/aws/ecs

%files elasticache
%{_libdir}/lib*elasticache.so

%files elasticache-devel
%{_includedir}/aws/elasticache

%files elasticbeanstalk
%{_libdir}/lib*elasticbeanstalk.so

%files elasticbeanstalk-devel
%{_includedir}/aws/elasticbeanstalk

%files elasticfilesystem
%{_libdir}/lib*elasticfilesystem.so

%files elasticfilesystem-devel
%{_includedir}/aws/elasticfilesystem

%files elasticloadbalancing
%{_libdir}/lib*elasticloadbalancing.so

%files elasticloadbalancing-devel
%{_includedir}/aws/elasticloadbalancing

%files elasticloadbalancingv2
%{_libdir}/lib*elasticloadbalancingv2.so

%files elasticloadbalancingv2-devel
%{_includedir}/aws/elasticloadbalancingv2

%files elasticmapreduce
%{_libdir}/lib*elasticmapreduce.so

%files elasticmapreduce-devel
%{_includedir}/aws/elasticmapreduce

%files elastictranscoder
%{_libdir}/lib*elastictranscoder.so

%files elastictranscoder-devel
%{_includedir}/aws/elastictranscoder

%files email
%{_libdir}/lib*email.so

%files email-devel
%{_includedir}/aws/email

%files es
%{_libdir}/lib*es.so

%files es-devel
%{_includedir}/aws/es

%files events
%{_libdir}/lib*events.so

%files events-devel
%{_includedir}/aws/events

%files firehose
%{_libdir}/lib*firehose.so

%files firehose-devel
%{_includedir}/aws/firehose

%files gamelift
%{_libdir}/lib*gamelift.so

%files gamelift-devel
%{_includedir}/aws/gamelift

%files glacier
%{_libdir}/lib*glacier.so

%files glacier-devel
%{_includedir}/aws/glacier

%files health
%{_libdir}/lib*health.so

%files health-devel
%{_includedir}/aws/health

%files iam
%{_libdir}/lib*iam.so

%files iam-devel
%{_includedir}/aws/iam

%files identity-management
%{_libdir}/lib*identity-management.so

%files identity-management-devel
%{_includedir}/aws/identity-management

%files importexport
%{_libdir}/lib*importexport.so

%files importexport-devel
%{_includedir}/aws/importexport

%files inspector
%{_libdir}/lib*inspector.so

%files inspector-devel
%{_includedir}/aws/inspector

%files iot
%{_libdir}/lib*iot.so

%files iot-devel
%{_includedir}/aws/iot

%files kinesisanalytics
%{_libdir}/lib*kinesisanalytics.so

%files kinesisanalytics-devel
%{_includedir}/aws/kinesisanalytics

%files kinesis
%{_libdir}/lib*kinesis.so

%files kinesis-devel
%{_includedir}/aws/kinesis

%files kms
%{_libdir}/lib*kms.so

%files kms-devel
%{_includedir}/aws/kms

%files lambda
%{_libdir}/lib*lambda.so

%files lambda-devel
%{_includedir}/aws/lambda

%files lightsail
%{_libdir}/lib*lightsail.so

%files lightsail-devel
%{_includedir}/aws/lightsail

%files logs
%{_libdir}/lib*logs.so

%files logs-devel
%{_includedir}/aws/logs

%files machinelearning
%{_libdir}/lib*machinelearning.so

%files machinelearning-devel
%{_includedir}/aws/machinelearning

%files marketplacecommerceanalytics
%{_libdir}/lib*marketplacecommerceanalytics.so

%files marketplacecommerceanalytics-devel
%{_includedir}/aws/marketplacecommerceanalytics

%files meteringmarketplace
%{_libdir}/lib*meteringmarketplace.so

%files meteringmarketplace-devel
%{_includedir}/aws/meteringmarketplace

%files mobileanalytics
%{_libdir}/lib*mobileanalytics.so

%files mobileanalytics-devel
%{_includedir}/aws/mobileanalytics

%files monitoring
%{_libdir}/lib*monitoring.so

%files monitoring-devel
%{_includedir}/aws/monitoring

%files opsworkscm
%{_libdir}/lib*opsworkscm.so

%files opsworkscm-devel
%{_includedir}/aws/opsworkscm

%files opsworks
%{_libdir}/lib*opsworks.so

%files opsworks-devel
%{_includedir}/aws/opsworks

%files polly
%{_libdir}/lib*polly.so

%files polly-devel
%{_includedir}/aws/polly

%files queues
%{_libdir}/lib*queues.so

%files queues-devel
%{_includedir}/aws/queues

%files rds
%{_libdir}/lib*rds.so

%files rds-devel
%{_includedir}/aws/rds

%files redshift
%{_libdir}/lib*redshift.so

%files redshift-devel
%{_includedir}/aws/redshift

%files rekognition
%{_libdir}/lib*rekognition.so

%files rekognition-devel
%{_includedir}/aws/rekognition

%files route53domains
%{_libdir}/lib*route53domains.so

%files route53domains-devel
%{_includedir}/aws/route53domains

%files route53
%{_libdir}/lib*route53.so

%files route53-devel
%{_includedir}/aws/route53

%files s3-encryption
%{_libdir}/lib*s3-encryption.so

%files s3-encryption-devel
%{_includedir}/aws/s3-encryption

%files s3
%{_libdir}/lib*s3.so

%files s3-devel
%{_includedir}/aws/s3

%files sdb
%{_libdir}/lib*sdb.so

%files sdb-devel
%{_includedir}/aws/sdb

%files servicecatalog
%{_libdir}/lib*servicecatalog.so

%files servicecatalog-devel
%{_includedir}/aws/servicecatalog

%files shield
%{_libdir}/lib*shield.so

%files shield-devel
%{_includedir}/aws/shield

%files snowball
%{_libdir}/lib*snowball.so

%files snowball-devel
%{_includedir}/aws/snowball

%files sns
%{_libdir}/lib*sns.so

%files sns-devel
%{_includedir}/aws/sns

%files sqs
%{_libdir}/lib*sqs.so

%files sqs-devel
%{_includedir}/aws/sqs

%files ssm
%{_libdir}/lib*ssm.so

%files ssm-devel
%{_includedir}/aws/ssm

%files states
%{_libdir}/lib*states.so

%files states-devel
%{_includedir}/aws/states

%files storagegateway
%{_libdir}/lib*storagegateway.so

%files storagegateway-devel
%{_includedir}/aws/storagegateway

%files sts
%{_libdir}/lib*sts.so

%files sts-devel
%{_includedir}/aws/sts

%files support
%{_libdir}/lib*support.so

%files support-devel
%{_includedir}/aws/support

%files swf
%{_libdir}/lib*swf.so

%files swf-devel
%{_includedir}/aws/swf

%files transfer
%{_libdir}/lib*transfer.so

%files transfer-devel
%{_includedir}/aws/transfer

%files waf
%{_libdir}/lib*waf.so

%files waf-devel
%{_includedir}/aws/waf

%files workspaces
%{_libdir}/lib*workspaces.so

%files workspaces-devel
%{_includedir}/aws/workspaces

%files xray
%{_libdir}/lib*xray.so

%files xray-devel
%{_includedir}/aws/xray

%changelog
