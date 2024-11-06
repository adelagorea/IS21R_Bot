const fs = require("fs");
const Table = require("cli-table3");

// Function to load and parse JSON data from a file
function loadJSON(file) {
  const data = fs.readFileSync(file, "utf-8");
  return JSON.parse(data);
}

// Function to get a map of IDs to car models from a dataset
function getIdToModelMap(dataset) {
  return dataset.reduce((acc, item) => {
    acc[item.id] = item.title;
    return acc;
  }, {});
}

// Function to get the IDs from a dataset
function getIds(dataset) {
  return dataset.map((item) => item.id);
}

// Function to compare two datasets and get the disappeared IDs
function getDisappearedIds(oldDataset, newDataset) {
  const oldIds = getIds(oldDataset);
  const newIds = new Set(getIds(newDataset));
  return oldIds.filter((id) => !newIds.has(id));
}

// Function to count occurrences of car models
function countModelOccurrences(ids, idToModelMap) {
  return ids.reduce((acc, id) => {
    const model = idToModelMap[id];
    acc[model] = (acc[model] || 0) + 1;
    return acc;
  }, {});
}

// Function to rank car models by the number of times they were sold
function rankModelsBySales(counts) {
  return Object.entries(counts)
    .sort((a, b) => b[1] - a[1])
    .map(([model, count]) => ({ model, count }));
}

// Load datasets
const oldDataset = loadJSON("scrapped_2024_06_08.json");
const newDataset = loadJSON("scrapped_2024_11_06.json");

// Get the map of IDs to car models from the old dataset
const idToModelMap = getIdToModelMap(oldDataset);

// Get disappeared IDs
const disappearedIds = getDisappearedIds(oldDataset, newDataset);

// Count occurrences of each car model for the disappeared IDs
const modelCounts = countModelOccurrences(disappearedIds, idToModelMap);

// Rank car models by the number of times they were sold
const rankedModels = rankModelsBySales(modelCounts);

// Save the ranked car models to a file
fs.writeFileSync(
  "rankedModels.json",
  JSON.stringify(rankedModels, null, 4),
  "utf-8"
);

console.log(
  "The ranking of the most sold car models has been saved to rankedModels.json"
);

// Display the top-10 rankings in a table in the console
const table = new Table({
  head: ["Rank", "Car Model", "Count"],
  colWidths: [6, 30, 10],
});

rankedModels.slice(0, 10).forEach((model, index) => {
  table.push([index + 1, model.model, model.count]);
});

console.log(table.toString());
