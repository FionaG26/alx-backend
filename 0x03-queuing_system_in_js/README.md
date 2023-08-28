# Queuing System in JavaScript (0x03)

This project focuses on building a queuing system in JavaScript for back-end development using NodeJS, ExpressJS, and Redis. It also introduces concepts of asynchronous operations, Redis server setup, and using the Kue library for job queueing.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Tasks](#tasks)
  1. [Install a Redis Instance](#1-install-a-redis-instance)
  2. [Node Redis Client](#2-node-redis-client)
  3. [Node Redis Client and Basic Operations](#3-node-redis-client-and-basic-operations)
  4. [Node Redis Client and Async Operations](#4-node-redis-client-and-async-operations)
  5. [Node Redis Client and Advanced Operations](#5-node-redis-client-and-advanced-operations)
  6. [Node Redis Client Publisher and Subscriber](#6-node-redis-client-publisher-and-subscriber)
  7. [Create the Job Creator](#7-create-the-job-creator)
  8. [Create the Job Processor](#8-create-the-job-processor)
  9. [Track Progress and Errors with Kue: Create the Job Creator](#9-track-progress-and-errors-with-kue-create-the-job-creator)
  10. [Track Progress and Errors with Kue: Create the Job Processor](#10-track-progress-and-errors-with-kue-create-the-job-processor)
  11. [Writing the Job Creation Function](#11-writing-the-job-creation-function)
  12. [Writing the Test for Job Creation](#12-writing-the-test-for-job-creation)
- [In Stock?](#in-stock)
  - [Data](#data)
  - [Data Access](#data-access)
  - [Server](#server)
  - [Products](#products)
  - [In Stock in Redis](#in-stock-in-redis)
  - [Product Detail](#product-detail)
  - [Reserve a Product](#reserve-a-product)

## Introduction

This project aims to build a queuing system in JavaScript, focusing on back-end development. It utilizes NodeJS, ExpressJS, Redis, and the Kue library. The queuing system is designed to handle asynchronous operations efficiently.

## Features

- Redis-based queuing system.
- Node Redis client for basic and advanced operations.
- Asynchronous task handling.
- Job creation and processing using the Kue library.
- Tracking job progress and handling errors.

## Resources

Before starting this project, it's recommended to read or watch the following resources:

- [Redis Quick Start](https://redis.io/topics/quickstart)
- [Redis Client Interface](https://redis.io/topics/rediscli)
- [Redis Client for Node.js](https://github.com/NodeRedis/node-redis)
- [Kue - Deprecated but Still Used in the Industry](https://github.com/Automattic/kue)

## Learning Objectives

By the end of this project, you should be able to explain the following concepts and perform the associated tasks without external assistance:

- Setting up a Redis server on your machine.
- Executing basic operations with the Redis client.
- Using a Redis client with Node.js for basic operations.
- Storing hash values in Redis.
- Handling asynchronous operations with Redis.
- Implementing Kue as a queuing system.
- Building a basic Express application that interacts with a Redis server.
- Extending the Express app to work with Redis and a job queue.

## Requirements

To successfully complete this project, ensure that you meet the following requirements:

- All code should be compiled/interpreted on Ubuntu 18.04, using Node 12.x and Redis 5.0.7.
- All code files should end with a new line.
- A `README.md` file must be present at the root of the project folder.
- Use the `.js` file extension for your code files.
- Required files for the project include `package.json`, `.babelrc`, and others as specified in the tasks.

## Project Structure

The project directory structure is as follows:

- `package.json`: Project configuration and dependencies.
- `.babelrc`: Babel configuration file.
- Various task-specific JavaScript files.

## Tasks

### 1. Install a Redis Instance

**Description:** Download, extract, and compile the latest stable Redis version. Start Redis in the background, set values, and verify its functionality.

### 2. Node Redis Client

**Description:** Install the `node_redis` library using npm. Create a script that connects to the Redis server and logs connection status.

### 3. Node Redis Client and Basic Operations

**Description:** Build a script that connects to the Redis server and performs basic operations like setting and getting values.

### 4. Node Redis Client and Async Operations

**Description:** Extend the previous script to handle asynchronous Redis operations, including error handling.

### 5. Node Redis Client and Advanced Operations

**Description:** Develop a script that demonstrates advanced Redis operations such as handling lists, sets, and hashes.

### 6. Node Redis Client Publisher and Subscriber

**Description:** Create two scripts - one for publishing and another for subscribing to channels in Redis.

### 7. Create the Job Creator

**Description:** Implement a script for creating jobs and adding them to a Redis job queue using the Kue library.

### 8. Create the Job Processor

**Description:** Build a script that processes jobs from the Redis job queue using the Kue library.

### 9. Track Progress and Errors with Kue: Create the Job Creator

**Description:** Enhance the job creation script to track job progress and handle errors using Kue.

### 10. Track Progress and Errors with Kue: Create the Job Processor

**Description:** Extend the job processing script to handle progress updates and errors using Kue.

### 11. Writing the Job Creation Function

**Description:** Create a function that generates and enqueues jobs for a specific task.

### 12. Writing the Test for Job Creation

**Description:** Develop a test script for the job creation function to ensure it functions correctly.

## In Stock?

### Data

- Assume there's a JSON file named `data.json` containing product data.
- Each product has an `id`, `name`, and `quantity` field.

### Data Access

- Implement a function to read this data from `data.json` and store it in Redis.

### Server

- Create an Express server to serve the following endpoints:

  - **GET /products**: Return a list of all products with their `id`, `name`, and `quantity`.
  - **GET /product/:id**: Return the product's `id`, `name`, and `quantity`.
  - **POST /reserve/:id**: Reserve one quantity of the product with the given `id`. If the product is not in stock, return an error message.
  - **POST /purchase/:id**: Purchase one quantity of the product with the given `id`. If the product is not in stock or not reserved, return an error message.

### Products

- Create a Redis hash for each product with fields `id`, `name`, and `quantity`.

### In Stock in Redis

- Use a Redis set to keep track of the products that are in stock.

### Product Detail

- Store the product details in a Redis hash.

### Reserve a Product

- When a product is reserved, decrement its quantity and add the user to a set of users who have reserved it.

---

This README provides an overview of the queuing system project in JavaScript. Follow the tasks step by step to implement the queuing system, and also implement the "In Stock?" functionality using Redis for product data management and an Express server to interact with it. Good luck!

