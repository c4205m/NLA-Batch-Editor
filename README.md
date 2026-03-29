
# NLA Batch Editor

<div align="center">
  <div>
    <img src="https://www.blender.org/wp-content/uploads/2020/07/blender_logo_no_socket_white.png" height="100" alt="Blender">
  </div>
  <div>
    <img src="https://img.shields.io/badge/Blender-Addon-green" alt="Blender Addon">
  </div>
  <p>A powerful Blender addon for batch editing Non-Linear Animation (NLA) strips and tracks.</p>
</div>

## Overview

NLA Batch Editor is designed to streamline the workflow on NLA Editor of Blender. It provides a comprehensive set of tools for batch operations, making it easier to manage and modify multiple NLA elements simultaneously.

## Features

  

### Batch Pushdown

- Push down multiple selected objects' actions to NLA strips

- Track and strip renaming on pushdown

- Random start frame options

- Control over mute states

- Preserve actions on pushdown

  

### Selection Management

- Advanced selection tools for NLA strips and tracks

- Filter-based selection options

- Transfer selection between tracks and strips

  

### Track Editing

- Batch track data modifications

- Toggle or set mute/lock states

- Track duplication capabilities

- Custom track naming options

  

### Strip Editing

- Batch strip data modification

- Comprehensive strip property controls


## Why Use NLA Batch Editor?

Managing multiple animations in Blender can quickly become tedious —especially when dealing with multiple objects, repeated actions, or preparing content for WebGL, Three.js, or glTF/GLB exports.

When preparing GLB files for web development, if you're animating multiple objects this helps you:
- Push down actions across multiple selected objects in one go
- Batch rename tracks and strips for clean, organized animation layers (This especially useful when multiple objects need to animate in sync. By assigning them the same identifier, you can trigger all related animations with a single call)

When dealing with poupulated NLA, NBE makes it easy to:
- Batch rename or duplicate strips and tracks
- Apply settings like blend in/out across multiple strips
- Set mute/lock states across many items simultaneously
- Selection filters based on names, states, and properties
- The ability to transfer selections between strips and tracks

Ultimately, the add-on empowers you to focus on *animation logic*, not *editor busywork*. Whether you’re cleaning up hundreds of strips or prepping a web-ready GLB file with clear structure and reusable components.


## Requirements

  

- Blender 4.1.0 or newer

- Python 3.x

  

## Installation

  
Download from the [Blender Extensions Platform](LINK). 

## Usage

  

The addon adds several panels to the NLA Editor's sidebar:

  

1.  **NBE | Batch Pushdown**

- Access batch pushdown operations

- Configure track and strip naming

- Set frame start options

  

2.  **NBE | Batch Edit**

- Selection management tools

- Track editing capabilities

- Strip editing functions
