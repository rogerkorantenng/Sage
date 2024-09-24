#!/bin/bash
# This script is executed at the beginning of the container build process.
# It configures the environment, installs necessary packages, sets the timezone, and performs cleanup.

# Set environment to non-interactive to avoid prompts during installation
export DEBIAN_FRONTEND=noninteractive

# Update the package list
sudo -E apt-get update

# Install essential packages with minimal dependencies
sudo -E apt-get install -y --no-install-recommends tzdata cmake zip unzip

# Set the system timezone to UTC
sudo -E ln -fs /usr/share/zoneinfo/Etc/UTC /etc/localtime
sudo -E dpkg-reconfigure --frontend noninteractive tzdata

# Clean up to reduce the image size
sudo -E apt-get clean
sudo -E rm -rf /var/lib/apt/lists/*

# Create the directory for documentation
sudo -E mkdir -p /mnt/docs
