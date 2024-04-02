# Chess Winner Predictor: Predicting Chess Game Outcomes with Machine Learning

Predicting the winner of chess games using machine learning techniques.

## Overview

Chess Winner Predictor is a project designed to predict the outcome of chess games based on various features such as game duration, player ratings, opening moves, and more. By leveraging historical chess game data and applying machine learning algorithms, this project provides a tool for predicting the likely winner of a given game.

## Features

- Predict the winner of a chess game based on various game features.
- Analyze historical game data to identify patterns and trends.
- Evaluate model performance using accuracy and other relevant metrics.
- Provide insights into key factors influencing game outcomes.

## Dataset

The dataset used in this project is sourced from the Lichess database, a popular online chess platform. It contains a collection of chess game records, including the following features:

### Numerical Features
- `turns`: Number of turns in the game.
- `white_rating`: Rating of the white player.
- `black_rating`: Rating of the black player.
- `opening_ply`: Number of moves in the opening phase of the game.

### Categorical Features
- `rated`: Whether the game was rated or not.
- `victory_status`: Outcome of the game (e.g., checkmate, draw).
- `increment_code`: Time control settings for the game.
- `opening_eco`: ECO (Encyclopaedia of Chess Openings) code representing the opening moves played.

The dataset is available in CSV format and is included in the `dataset` directory of this repository.

## Installation

1. Clone the repository:

2. Install the required dependencies:


## Usage

1. Ensure you have Python and the necessary libraries installed.
2. Download the dataset (if not already provided) and place it in the project directory.
3. Run the main script to preprocess the data, train the model, and make predictions:
4. Explore the results and evaluate the model's performance.

## End Results

From the obtained results, the ensemble model composed of Gradient Boosting Classifiers achieved the highest model performance with an accuracy of 88.8%. As a result, the model has been saved to the file 'chess_winner_predictor_model.pkl'.
