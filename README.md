# Table of Contents
- [Introduction](#nvidia-ai-workbench-introduction)
   - [Project Description](#project-description)
   - [Prerequisites](#prerequisites)
- [Quickstart](#quickstart)
   - [Using Local Development Environment](#using-local-development-environment)
   - [Using a Cloud Development Environment](#using-a-cloud-development-environment)

# NVIDIA AI Workbench: Introduction [![Open In AI Workbench](https://img.shields.io/badge/Open_In-AI_Workbench-76B900)](https://nvidia.github.io/workbench-example-hybrid-rag/clone_me.html)

## Project Description
This project focuses on developing a Gemma Model application with a customizable Gradio Chat app. Key features include:
- Interacting with a personalized chatbot that serves as your assistant.
- Running inference **locally** on the model.

### Table 1: Default Supported Models by Inference Mode

<details>
<summary><b>Expand this section for a full table on all supported models by inference mode.</b></summary>

<!-- Table contents go here -->

</details>

## Prerequisites
- A Kaggle account is required to generate a username and key.

---

## System Requirements
Below are the minimum and recommended system requirements for the project:

| vRAM  | System RAM | Disk Storage | vCPU         | GPU                   |
|-------|------------|--------------|--------------|-----------------------|
| 16 GB | 32 GB      | 70 GB        | Intel Core i7| At least 1 (optional) |

## Getting Your Kaggle Username and Key
1. Log in to [Kaggle](https://www.kaggle.com/) and navigate to your account settings.

   ![Kaggle Profile](https://christianjmills.com/posts/kaggle-obtain-api-key-tutorial/images/kaggle-click-profile-picture.png)


2. In the pop-up window, click on "Settings".

   ![Kaggle Settings](https://christianjmills.com/posts/kaggle-obtain-api-key-tutorial/images/kaggle-click-settings-menu-option.png)


3. Scroll down to the "API" section and click on "Create New API Token".

   ![Create API Token](https://christianjmills.com/posts/kaggle-obtain-api-key-tutorial/images/kaggle-account-settings-click-create-new-token.png)


4. This will download a `kaggle.json` file to your computer.

   ![Download kaggle.json](https://christianjmills.com/posts/kaggle-obtain-api-key-tutorial/images/kaggle-save-kaggle-json-file.png)


5. Open the file and copy the `username` and `key` fields.


## Quickstart

### Using Local Development Environment

1. **Install and Set Up AI Workbench**: Begin by [installing and configuring](https://docs.nvidia.com/ai-workbench/user-guide/latest/installation/overview.html) AI Workbench on your local machine. Open the application and select a preferred location.

2. **Fork the Repository**: Fork this repository into your own GitHub account.

3. **Clone the Project in AI Workbench**:
   - Inside AI Workbench, click on **Clone Project**.
   - Enter the URL of your forked repository.
   - AI Workbench will clone the repository and build the project environment. This process may take several minutes.

4. **Configure Environment Variables**:
   - Once the build is complete, navigate to **Environment** > **Variable** > **KAGGLE_USERNAME** > **Configure** and enter your Kaggle Username as a project variable.
   - Similarly, navigate to **Environment** > **Variable** > **KAGGLE_KEY** > **Configure** and enter your Kaggle API Key.

5. **Start the Project**:
   - Click on **Start Environment** to launch the project container.
   - To open the Gradio app, select **Open Chat** from the top right corner of the AI Workbench window. The app will open in your browser.

### Using a Cloud Development Environment

1. **Set Up an AWS EC2 Instance**:
   - Log in to your AWS Management Console.
   - Navigate to **EC2 Dashboard** > **Launch Instance**.
   - Choose an appropriate Amazon Machine Image (AMI), preferably one with an NVIDIA GPU, such as an NVIDIA Deep Learning AMI.
   - Select an instance type with sufficient GPU resources (e.g., `g4dn.xlarge`).
   - Configure your instance, including network settings and storage, according to your project requirements.
   - Review and launch the instance. Ensure you have a key pair for SSH access.

2. **Connect to Your EC2 Instance**:
   - Open a terminal on your local machine.
   - Connect to your EC2 instance using SSH:
     ```bash
     ssh -i /path/to/your-key.pem ec2-user@your-ec2-public-ip
     ```
   - Replace `/path/to/your-key.pem` with the path to your private key and `your-ec2-public-ip` with your instance's public IP address.

3. **Install and Set Up AI Workbench on the EC2 Instance**:
   - Once connected to your EC2 instance, update your system:
     ```bash
     sudo apt-get update
     sudo apt-get upgrade
     ```
   - Follow the [official NVIDIA guide](https://docs.nvidia.com/ai-workbench/user-guide/latest/installation/ubuntu-remote.html) to install and set up AI Workbench on your EC2 instance. This guide provides detailed instructions for remote installation on Ubuntu systems.

4. **Clone the Project in AI Workbench**:
   - Inside AI Workbench on the EC2 instance, click on **Clone Project**.
   - Enter the URL of your forked repository.
   - AI Workbench will clone the repository and build the project environment. This process may take several minutes.

5. **Configure Environment Variables**:
   - Once the build is complete, navigate to **Environment** > **Variable** > **KAGGLE_USERNAME** > **Configure** and enter your Kaggle Username as a project variable.
   - Similarly, navigate to **Environment** > **Variable** > **KAGGLE_KEY** > **Configure** and enter your Kaggle API Key.

6. **Start the Project**:
   - Click on **Start Environment** to launch the project container.
   - To open the Gradio app, select **Open Chat** from the top right corner of the AI Workbench window. The app will open in your browser.
