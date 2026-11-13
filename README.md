# Internet Interactions Visual Novel

## Overview

The **Internet Interactions Visual Novel** is a single-player, story-driven game developed by the **Anti-Linear Algebra Club (ALA Club)**.

The goal of the project is to explore how people interact with others online and show both the positive and negative sides of internet relationships. The player progresses through a fictional friend-making platform where they meet different characters, make decisions, and experience the consequences of those decisions.

The story will explore topics such as:

- Online friendships
- Online relationships
- Cyberbullying
- Scams
- Misinformation
- Internet safety
- Trust and decision-making

Rather than presenting the internet as completely good or completely bad, the game is intended to show that online interactions depend heavily on the choices people make and how they respond to different situations.

## Current Project Stage

The project is currently in the **design and early development stage**.

Milestone 1 focused on defining:

- Stakeholders
- User personas
- Functional requirements
- Non-functional requirements
- Features
- User stories
- Acceptance criteria
- Use case diagrams
- Class diagrams
- Sequence diagrams

The next stage of the project will focus on turning these designs into a working game prototype.

## Core Gameplay

The player will begin by entering a custom name for the protagonist.

From there, the player will progress through an introductory story where they are introduced to a fictional online friend-making platform.

During the game, the player will:

- Read character dialogue
- Meet different characters
- Select dialogue and story choices
- Build or damage relationships
- Encounter different online situations
- Explore branching storylines
- Reach different endings
- Replay the story to make different decisions

Player decisions are intended to have noticeable effects on future scenes and character relationships.

## Planned Features

### Character Naming

Players can choose a custom name for the protagonist before beginning the story.

### Dialogue System

The game displays character dialogue and narrative information one section at a time.

### Choice System

Players are presented with multiple options during important interactions.

Choices are recorded and may affect later events.

### Branching Storylines

Previous decisions determine which scenes and character routes the player experiences.

### Character Routes

Different characters will have individual personalities, dialogue, relationships, and storylines.

### Relationship System

Important choices may increase or decrease relationship values with characters.

Relationship values can influence future interactions and endings.

### Multiple Endings

The game will evaluate previous decisions, relationships, and story progression to determine which ending the player receives.

### Save and Load

Players will be able to save their current progress and return to the story later.

### Replayability

Players can restart the story and choose different options to discover alternative routes and endings.

## Game Structure

The current system design separates the game into several major components.

### Game

Coordinates the major systems and starts or restarts gameplay.

### Player

Stores information related to the player character, including the custom protagonist name.

### Story Manager

Controls the current story state, loads scenes, advances the story, and processes player decisions.

### Story

Contains the collection of scenes that make up the game's narrative.

### Scene

Contains information needed for an individual part of the story, including:

- Scene ID
- Background
- Dialogue
- Available choices

### Dialogue

Stores the character speaking and the text being displayed.

### Choice

Represents a decision the player can make and determines where the story may go next.

### Character

Represents the different people that the player meets throughout the game.

### Relationship

Tracks relationship values between the protagonist and other characters.

### Ending Manager

Checks the player's decisions, relationships, and story progress to determine which ending should occur.

### Save Manager

Handles saving and loading the player's story progress.

## Example Gameplay Flow

A basic playthrough may follow this structure:

`Start Game`

↓

`Enter Protagonist Name`

↓

`Introduction`

↓

`Join Fictional Friend-Making Platform`

↓

`Meet Characters`

↓

`Read Dialogue`

↓

`Make Choices`

↓

`Update Relationships / Story State`

↓

`Follow Story Branch`

↓

`Reach Ending`

Players can then restart the game and make different decisions to explore other story routes.

## Technology

The team is currently considering **Ren'Py** as the primary game engine because it is designed for visual novels and supports dialogue, branching choices, saving/loading, and story scripting.

The final technology and project structure may change as development progresses.

## Project Goals

The main goals of the project are to:

1. Create an interactive and replayable visual novel.
2. Make player decisions meaningfully affect the story.
3. Explore realistic online interactions and internet-related risks.
4. Create multiple characters and story routes.
5. Provide multiple endings based on player choices.
6. Build a working game using concepts from software engineering, including requirements engineering, system modeling, architecture, implementation, and testing.

## Team

### Anti-Linear Algebra Club

**Talon Sargent**  
Documentation and Testing

**Cody Adams**  
Backend, Data Management, Programming, Brainstorming, and Scenario Development

**Sean Kean**  
Frontend and UI/UX Design

Although members have primary areas of responsibility, the project is being developed collaboratively.

## Repository Structure

The repository structure will be updated as implementation begins.

A possible structure is:

```text
project/
├── game/
│   ├── scripts/
│   ├── characters/
│   ├── scenes/
│   ├── images/
│   ├── audio/
│   └── saves/
├── documentation/
│   ├── requirements/
│   ├── UML/
│   └── milestones/
├── README.md
└── LICENSE
```

The exact structure will depend on the final game engine and implementation approach.

## Development Status

🚧 **In Development**

Current focus:

**Requirements and System Design → Prototype Development**

The team has completed the initial requirements, feature planning, user stories, and UML system models. Development will continue by implementing and testing the main gameplay systems.

## Future Development

Future work will include implementing the game engine, creating the opening storyline, adding characters, developing branching decisions, tracking relationships, creating endings, implementing save/load support, testing story routes, and improving the game's user interface.

---

**CS 484 — Software Engineering Project**  
**Anti-Linear Algebra Club**
