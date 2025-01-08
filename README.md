# Unitree Robot Control Framework for Human Activity Recognition
Overview
This project, developed by the team of researchers at SDSU's DiCE Lab, introduces a high-level control framework for Unitree quadruped robots. Specifically designed to facilitate integration with Building Information Models (BIM) and Unity-based simulations, our project includes an example configuration that performs human activity recognition (HAR) in a construction environment. The framework simplifies mission planning and enhances the adaptability of Unitree robots for various applications. The Python backend provides modular, client-server-based functionality to facilitate communication between robots, edge devices, sensors, and APIs, supporting rapid deployment for non-experts in robotics.

Key Features:
BIM Integration: Uses BIM data for mission planning with Unity.
Modular Design: A Python client-server architecture for simplified customization and scalability.
Human Activity Recognition Example: Implementation of HAR with real-time data processing and dynamic labeling of inference data.
The source code for this project, along with a construction-specific case study demonstrating its capabilities, is available in this repository.

# Highlight: Explainable AI Feature by Robert Ashe

As part of this project, I implemented the Explainable AI (XAI) feature, designed to generate natural language explanations for AI inferenced made during HAR. This functionality was developed to enhance trust and transparency in human-robot collaboration. My contributions include:

1. Development of explain_processor.py
The core logic for the XAI feature is contained in the explain_processor.py file.  This module extracts key video frames and encodes them for efficient use, then gathers other state data that represents an inference made by the HAR module. Explanations are generated using the collected state data and OpenAI's GPT model, then saved alongside corresponding auto-labeled video data for traceability.

2. Client and Server Integration
I integrated the XAI feature into the broader framework by implementing the framework's client and server components that enable communication between Unity, the Python backend, and the robot. The modular architecture of the Python backend facilitated rapid integration of customizations, simplifying the deployment of features on the Unitree Go1 robot we used in development.





