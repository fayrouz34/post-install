#!/bin/bash
import os

print("UBUNTU POST-INSTALL SCRIPT")

print("Updating APT...")

os.system("sudo apt-get update") 

os.system("clear")

print("Installing base packages")

os.system("sudo apt-get install --yes git git-extras build-essential python3-pip") 

print("install discord")

os.system("sudo snap install discord")

print("fin d'installation")