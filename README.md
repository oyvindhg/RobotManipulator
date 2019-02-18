# [AI Planning and Low-Level Control for a Robotic Manipulator](http://hdl.handle.net/11250/2563985)

**Description:** This repo contains all code used for my master's thesis for the Cybernetics and Robotics study program at NTNU. Feel free to read my master's thesis at the following page: http://hdl.handle.net/11250/2563985

## Thesis abstract
This thesis aims to explore the fusion of high-level AI planning and low-level robotic control. Although the field of AI planning can be said to have sprung out from robotics, researchers have recently expressed concern that the two fields have moved in separate directions even though there is great potential for development in their intersection. This has raised a number of open questions about how to best merge AI planning techniques with robotic control. This project explores some of these questions through the process of building an autonomous robot system.

Three modules formed the building blocks of the system: The control module, the perception module and the planning module. The control module was made by setting up a custom-built robot manipulator and enhancing it with inverse kinematics control of its movements. The perception module made use of a Kinect sensor to take RBG and depth images of the environment and analyzed the images using deep learning in order to detect objects. The perception module also determined the location of the detected objects. The planning module consisted of a STRIPS planner that automatically designed series of actions for the robot to perform in order to bring the environment to a desired state.

The modules were merged into a robot system that was able to operate in a real-world environment. The data about the objects and their location in the environment was fed from the perception module to the planning module in order to create a model of the environment and to initialize the planning algorithm. The continuous execution monitoring performed by the cooperation between the perception and planning modules was shown to be able to handle a number of unexpected situations that happen in the real world. The robot was unavailable during the final tests, but the modular system was easily adjusted for this in order to work for simulated robot actions done by hand. This flexibility of the system would also allow it to be used for any other robotic manipulator by changing the robot measurement specifications.

The goal of creating a system merging AI planning with robotic control is considered achieved. A series of interesting ideas for expanding the system are left open for future research, and it is hoped that these ideas will be explored in the years to come by students and researchers, using the robotic system presented in this thesis as a foundation for their work.
