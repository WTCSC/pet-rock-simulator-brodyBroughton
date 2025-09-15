# Pet Rock Game

A simple command-line pet simulation game where you take care of a virtual pet rock. Keep your pet rock happy, fed, and energized to prevent it from meeting various amusing demises.

## Description

Pet Rock is a text-based game where players care for a virtual pet rock by managing three key stats: anger, hunger, and energy. The goal is to keep your pet rock alive by balancing these stats through various actions. The game features humorous death messages and requires strategic thinking to maintain proper care.

## Features

- **Pet Naming**: Choose a custom name for your pet rock (up to 16 characters)
- **Stat Management**: Monitor and manage three core stats:
  - Anger (0-10)
  - Hunger (0-10) 
  - Energy (0-10)
- **Interactive Actions**:
  - Pet your rock to reduce anger
  - Feed your rock to reduce hunger
  - Give energy drinks to boost energy
  - Do nothing (skip turn)
- **Game Over Conditions**: Multiple amusing ways your pet rock can meet its end
- **Real-time Stats Display**: View current stats after each turn

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Download the `pet_rock.py` file
2. No additional dependencies required

### Running the Game

```bash
python pet_rock.py
```

## How to Play

1. **Start the Game**: Run the script and enter a name for your pet rock
2. **Monitor Stats**: Keep track of your pet's anger, hunger, and energy levels
3. **Choose Actions**: Select from the available actions each turn:
   - `1` - Pet your rock (reduces anger by 2)
   - `2` - Feed your rock (reduces hunger by 2)
   - `3` - Give energy drink (increases energy by 5)
   - `4` - Do nothing
4. **Survive**: Keep all stats within safe ranges to avoid game over

### Game Mechanics

- **Stat Ranges**: All stats range from 0-10
- **Automatic Changes**: Each turn, hunger and anger increase by 1, energy decreases by 1
- **Win Condition**: There is no traditional win condition - the goal is survival
- **Loss Conditions**:
  - Anger ≥ 10: Pet rock combusts
  - Hunger ≥ 10: Pet rock dies of hunger
  - Energy ≥ 10: Pet rock becomes a neutron star
  - Energy ≤ 0: Pet rock dies from exhaustion

## Game Strategy

- Balance is key - don't let any stat reach dangerous levels
- Plan ahead considering the automatic stat changes each turn
- Energy drinks are powerful but dangerous if overused
- Regular feeding and petting help maintain baseline stats

## File Structure

```
pet_rock.py          # Main game file containing all functions
```

### Key Functions

- `get_pet_name()`: Handles pet name input with validation
- `main_loop(stats)`: Core game loop managing stats and actions
- `main()`: Initializes game and starts the main loop

## Contributing

This is a simple educational project. Feel free to fork and modify for learning purposes.

## License

This project is provided as-is for educational purposes.