const fs = require("fs");

// Function to load and parse JSON data from a file
function loadJSON(filename) {
  const rawData = fs.readFileSync(filename, "utf-8");
  return JSON.parse(rawData);
}

// Function to count car models in a data set
function countCarModels(data) {
  const modelCount = {};

  data.forEach((item) => {
    const model = item.title.split(",")[0]; // Assuming the model is the first word in the title
    if (modelCount[model]) {
      modelCount[model]++;
    } else {
      modelCount[model] = 1;
    }
  });

  return modelCount;
}

// Function to sort car models by count in descending order
function sortCarModelsByCount(modelCount) {
  return Object.entries(modelCount)
    .sort(([, countA], [, countB]) => countB - countA)
    .map(([model, count]) => ({ model, count }));
}

// Load and parse the JSON data set
const data = loadJSON("scrapped_2024_06_08.json"); // Replace with the actual file name

// Count car models in the data set
const modelCount = countCarModels(data);

// Sort car models by count
const sortedModels = sortCarModelsByCount(modelCount);

// Print the top 20 sold car models
console.log("Top 20 Sold Car Models:");
sortedModels.slice(0, 20).forEach(({ model, count }, index) => {
  console.log(`${index + 1}. ${model}: ${count} sales`);
});
