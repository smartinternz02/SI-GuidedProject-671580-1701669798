document.getElementById('predictionForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get input values
    const closedAt = document.getElementById('closedAt').value.trim();
    const relationships = parseFloat(document.getElementById('relationships').value);
    const milestones = parseFloat(document.getElementById('milestones').value);
    const isTop500 = document.getElementById('isTop500').value;
    const ageLastMilestoneYear = parseFloat(document.getElementById('ageLastMilestoneYear').value);
    const hasRoundB = document.getElementById('hasRoundB').value;
    const fundingRounds = parseFloat(document.getElementById('fundingRounds').value);
    const ageParticipants = parseFloat(document.getElementById('ageParticipants').value);
    const hasRoundA = document.getElementById('hasRoundA').value;

    // Calculate total score
    const totalScore = relationships + milestones -
                       (isTop500 === 'yes' ? 1 : 0) -
                       (ageLastMilestoneYear / 10) +
                       (hasRoundB === 'yes' ? 2 : 0) +
                       (fundingRounds * 0.25) -
                       (ageParticipants / 5) +
                       (hasRoundA === 'yes' ? 1 : 0);

    // Determine prediction result
    let predictionResult;
    if (totalScore >= 0) {
        predictionResult = 'Success';
    } else {
        predictionResult = 'Fail';
    }

    // Display prediction result
    const resultElement = document.getElementById('predictionResult');
    resultElement.textContent = `Prediction: ${predictionResult}`;
});
