const Workout = require("../database/Workout");
const getAllWorkouts = () => {
    const AllWorkouts = Workout.getAllWorkouts();
    return AllWorkouts;
};

const getOneWorkout = () => {
  return;
};

const createNewWorkout = () => {
  return;
};

const updateOneWorkout = () => {
  return;
};

const deleteOneWorkout = () => {
  return;
};

module.exports = {
  getAllWorkouts,
  getOneWorkout,
  createNewWorkout,
  updateOneWorkout,
  deleteOneWorkout,
};