export async function fetchModelFeatures(model) {
  const response = await fetch(`http://localhost:5000/features/${model}`);
  if (!response.ok) {
    throw new Error("Failed to fetch model features");
  }
  const data = await response.json();
  return data.features.map((f) => f.replace("x.", "")); // Remove 'x.' prefix
}

export async function sendPrediction(formData, model) {
  const formattedData = {};
  Object.keys(formData).forEach((key) => {
    formattedData[`x.${key}`] = parseFloat(formData[key]) || 0;
  });

  const response = await fetch(`http://localhost:5000/predict/${model}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(formattedData),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.error || "Failed to get prediction");
  }

  return response.json();
}
