import { Student } from "../models/Student.js";
import { spawn } from "child_process";
import { exec } from "child_process";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export const predictStudentResult = async (req, res) => {
    try {
        const student = await Student.findOne({
            _id: req.params.studentId,
            teacher: req.teacher.id,
        });

        if (!student) {
            return res.status(404).json({ statusCode: 404, message: "Student not found" });
        }

        // Check if student has required data for prediction
        if (student.attendance === undefined || student.studyHours === undefined ||
            student.previousMarks === undefined || student.assignmentScore === undefined) {
            return res.status(400).json({
                statusCode: 400,
                message: "Student data is incomplete for prediction. Missing required fields."
            });
        }

        // Prepare input data for the Python script as JSON
        const inputData = {
            attendance: student.attendance,
            study_hours: student.studyHours,
            previous_marks: student.previousMarks,
            assignment_score: student.assignmentScore
        };

        // Correct path resolution: from controllers to src root then to microservice
        const microserviceDir = path.join(__dirname, "..", "..", "microservice");
        const pythonScriptPath = path.join(microserviceDir, "predict.py");

        // Check if Python is available
        exec("python3 --version", (error, stdout, stderr) => {
            if (error) {
                // Try with python instead of python3
                exec("python --version", (error2, stdout2, stderr2) => {
                    if (error2) {
                        console.error("Python execution error:", error2);
                        return res.status(500).json({
                            statusCode: 500,
                            message: "Python is not installed or not available in system PATH. Please install Python and ensure it's in your PATH. Error: " + error2.message
                        });
                    }

                    // Python is available, proceed with the prediction
                    const py = spawn("python3", [
                        pythonScriptPath, // Use absolute path
                        JSON.stringify(inputData)  // Pass JSON string as single argument
                    ], {
                        cwd: path.join(__dirname, "../..") // Set working directory to server root
                    });

                    let output = "";
                    let errorOutput = "";

                    py.stdout.on("data", (data) => {
                        output += data.toString();
                    });

                    py.stderr.on("data", (err) => {
                        errorOutput += err.toString();
                        console.error("Python error:", err.toString());
                    });

                    py.on("close", async (code) => {
                        if (code !== 0) {
                            console.error("Python script exited with code:", code);
                            console.error("Error output:", errorOutput);
                            return res.status(500).json({
                                statusCode: 500,
                                message: `Prediction failed. Python script exited with code ${code}. Error: ${errorOutput}`
                            });
                        }

                        if (!output.trim()) {
                            console.error("No output from Python script");
                            return res.status(500).json({
                                statusCode: 500,
                                message: "Prediction failed. No output received from the prediction model."
                            });
                        }

                        // Save prediction
                        let outputResponse = {
                            predictedResult: output.trim(),
                            attendance: student.attendance,
                            studyHours: student.studyHours,
                            previousMarks: student.previousMarks,
                            assignmentScore: student.assignmentScore,
                        }
                        student.predictions.push(outputResponse);
                        await student.save();

                        res.status(200).json({
                            statusCode: 200,
                            message: `Prediction done successfully.`,
                            data: {
                                studentName: student.name,
                                prediction: outputResponse.predictedResult,
                            }
                        });
                    });

                    py.on("error", (err) => {
                        console.error("Python spawn error:", err);
                        return res.status(500).json({
                            statusCode: 500,
                            message: "Failed to execute Python prediction script: " + err.message
                        });
                    });
                });
                return;
            }

            // Python3 is available, proceed with the prediction
            const py = spawn("python3", [
                pythonScriptPath, // Use absolute path
                JSON.stringify(inputData)  // Pass JSON string as single argument
            ], {
                cwd: path.join(__dirname, "../..") // Set working directory to server root
            });

            let output = "";
            let errorOutput = "";

            py.stdout.on("data", (data) => {
                output += data.toString();
            });

            py.stderr.on("data", (err) => {
                errorOutput += err.toString();
                console.error("Python error:", err.toString());
            });

            py.on("close", async (code) => {
                if (code !== 0) {
                    console.error("Python script exited with code:", code);
                    console.error("Error output:", errorOutput);
                    return res.status(500).json({
                        statusCode: 500,
                        message: `Prediction failed. Python script exited with code ${code}. Error: ${errorOutput}`
                    });
                }

                if (!output.trim()) {
                    console.error("No output from Python script");
                    return res.status(500).json({
                        statusCode: 500,
                        message: "Prediction failed. No output received from the prediction model."
                    });
                }

                // Save prediction
                let outputResponse = {
                    predictedResult: output.trim(),
                    attendance: student.attendance,
                    studyHours: student.studyHours,
                    previousMarks: student.previousMarks,
                    assignmentScore: student.assignmentScore,
                }
                student.predictions.push(outputResponse);
                await student.save();

                res.status(200).json({
                    statusCode: 200,
                    message: `Prediction done successfully.`,
                    data: {
                        studentName: student.name,
                        prediction: outputResponse.predictedResult,
                    }
                });
            });

            py.on("error", (err) => {
                console.error("Python spawn error:", err);
                return res.status(500).json({
                    statusCode: 500,
                    message: "Failed to execute Python prediction script: " + err.message
                });
            });
        });

    } catch (error) {
        console.error("Error in predictStudentResult:", error);
        res.status(500).json({ statusCode: 500, message: error.message });
    }
};
