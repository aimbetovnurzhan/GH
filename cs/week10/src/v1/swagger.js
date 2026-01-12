const swaggerJSDoc = require("swagger-jsdoc");
const swaggerUi = require("swagger-ui-express");

// Basic Meta Informations about our API
const options = {
  definition: {
    openapi: "3.0.0",
    info: { title: "Crossfit WOD API", version: "1.0.0" },
  },
  apis: ["./src/v1/routes/workoutRoutes.js","./src/v1/swagger.js"],
};

/**
 * @openapi
 * components:
 *   schemas:
 *     Workout:
 *       type: object
 *       properties:
 *         id:
 *           type: string
 *           example: "a12b3c4d"
 *         name:
 *           type: string
 *           example: "Push Workout"
 *         mode:
 *           type: string
 *           example: "For time"
 *         equipment:
 *           type: array
 *           items:
 *             type: string
 *           example: ["barbell", "rope"]
 *         exercises:
 *           type: array
 *           items:
 *             type: string
 *           example: ["squat", "pull-up"]
 *         createdAt:
 *           type: string
 *           example: "2024-01-01T12:00:00Z"
 *         updatedAt:
 *           type: string
 *           example: "2024-01-01T12:00:00Z"
 *     Record:
 *       type: object
 *       properties:
 *         id:
 *           type: string
 *           example: "b7f9c2e1-4d3a-4c8a-9f1e-123456789abc"
 *         workout:
 *           type: string
 *           description: ID of the workout this record belongs to
 *           example: "4a3d9aaa-608c-49a7-a004-66305ad4ab50"
 *         record:
 *           type: string
 *           description: Performance result or time
 *           example: "12:45"
 *         member:
 *           type: string
 *           description: ID of the member who performed the workout
 *           example: "d1e2f3a4-5678-90ab-cdef-1234567890ab"
 *     Member:
 *       type: object
 *       properties:
 *         id:
 *           type: string
 *           example: "d1e2f3a4-5678-90ab-cdef-1234567890ab"
 *         name:
 *           type: string
 *           example: "John Doe"
 *         gender:
 *           type: string
 *           example: "male"
 *         age:
 *           type: integer
 *           example: 29
 *         createdAt:
 *           type: string
 *           example: "2024-01-01T12:00:00Z"
 *         updatedAt:
 *           type: string
 *           example: "2024-01-01T12:00:00Z"
 */

// Docs in JSON format
const swaggerSpec = swaggerJSDoc(options);

// Function to setup our docs
const swaggerDocs = (app, port) => {
  // Route-Handler to visit our docs
  app.use("/api/v1/docs", swaggerUi.serve, swaggerUi.setup(swaggerSpec));
  // Make our docs in JSON format available
  app.get("/api/v1/docs.json", (req, res) => {
    res.setHeader("Content-Type", "application/json");
    res.send(swaggerSpec);
  });
  console.log(
    `Version 1 Docs are available on http://localhost:${port}/api/v1/docs`
  );
};

module.exports = { swaggerDocs };