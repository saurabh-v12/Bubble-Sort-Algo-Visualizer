# Bubble Sort Algorithm Visualizer
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/saurabh-v12/Bubble-Sort-Algo-Visualizer)

This project provides a simple visualizer for the Bubble Sort algorithm, created using Python and the Pygame library. It helps in understanding the inner workings of Bubble Sort by representing an array as vertical bars and animating the comparison and swapping steps.

## Features

- **Visual Sorting:** An array of integers is displayed as a collection of bars, and the entire sorting process is animated.
- **Color-Coded Steps:** The visualizer uses colors to indicate the current operation:
  - **Blue Bars:** The default state of the array elements.
  - **Red Bars:** Highlights the two elements currently being compared.
  - **Green Bars:** Highlights the two elements that have just been swapped.
- **Interactive Controls:** You can control the flow of the visualization.
- **Adjustable Speed:** Increase or decrease the animation speed to observe the algorithm at your own pace.

## Prerequisites

- Python 3
- Pygame library

## Installation

1.  Clone the repository to your local machine:
    ```bash
    git clone https://github.com/saurabh-v12/Bubble-Sort-Algo-Visualizer.git
    cd Bubble-Sort-Algo-Visualizer
    ```

2.  Install the required Pygame library using pip:
    ```bash
    pip install pygame
    ```

## How to Run

Navigate to the project directory in your terminal and run the following command:

```bash
python bsv.py
```

A new window will open, displaying the randomly generated, unsorted array as bars.

## Controls

Use the following keyboard keys to interact with the visualizer:

-   **`SPACE`**: Start the sorting process.
-   **`R`**: Reset the visualizer with a new, randomly generated array.
-   **`UP ARROW`**: Increase the speed of the sorting animation.
-   **`DOWN ARROW`**: Decrease the speed of the sorting animation.
