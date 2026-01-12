const { v4: uuid } = require("uuid");
const Workout = require("../models/Workout");

const getAllWorkouts = async (filterParams) => {
  try {
    if (filterParams.mode) {
      return await Workout.find({
        mode: { $regex: filterParams.mode, $options: "i" },
      });
    }

    return await Workout.find();
  } catch (error) {
    throw error;
  }
};

const getOneWorkout = async (workoutId) => {
  try {
    const workout = await Workout.findOne({ id: workoutId });

    if (!workout) {
      throw {
        status: 400,
        message: `Can't find workout with id '${workoutId}'`,
      };
    }

    return workout;
  } catch (error) {
    throw error;
  }
};

const createNewWorkout = async (newWorkout) => {
  const workoutToInsert = {
    ...newWorkout,
    id: uuid(),
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
  };

  try {
    const exists = await Workout.findOne({ name: workoutToInsert.name });
    if (exists) {
      throw {
        status: 400,
        message: `Workout with the name '${workoutToInsert.name}' already exists`,
      };
    }

    const createdWorkout = await Workout.create(workoutToInsert);
    return createdWorkout;
  } catch (error) {
    throw error;
  }
};

const updateOneWorkout = async (workoutId, changes) => {
  try {
    const exists = await Workout.findOne({ name: changes.name });
    if (exists) {
      throw {
        status: 400,
        message: `Workout with the name '${changes.name}' already exists`,
      };
    }

    const updatedWorkout = await Workout.findOneAndUpdate(
      { id: workoutId },
      { ...changes, updatedAt: new Date().toISOString() },
      { new: true }
    );

    if (!updatedWorkout) {
      throw {
        status: 400,
        message: `Can't find workout with id '${workoutId}'`,
      };
    }

    return updatedWorkout;
  } catch (error) {
    throw error;
  }
};

const deleteOneWorkout = async (workoutId) => {
  try {
    const deleted = await Workout.findOneAndDelete({ id: workoutId });

    if (!deleted) {
      throw {
        status: 400,
        message: `Can't find workout with id '${workoutId}'`,
      };
    }
  } catch (error) {
    throw error;
  }
};

module.exports = {
  getAllWorkouts,
  getOneWorkout,
  createNewWorkout,
  updateOneWorkout,
  deleteOneWorkout,
};