
import json
import json.scanner


out= [[{'label': 'neutral', 'score': 0.9629464745521545}, {'label': 'approval', 'score': 0.020771488547325134}, {'label': 'realization', 'score': 0.007765655871480703}, {'label': 'annoyance', 'score': 0.007097587455064058}, {'label': 'admiration', 'score': 0.004355949815362692}, {'label': 'disapproval', 'score': 0.0038591763004660606}, {'label': 'disappointment', 'score': 0.0031303209252655506}, {'label': 'disgust', 'score': 0.002305078087374568}, {'label': 'excitement', 'score': 0.0021805046126246452}, {'label': 'anger', 'score': 0.002053138567134738}, {'label': 'sadness', 'score': 0.0018999186577275395}, {'label': 'joy', 'score': 0.0018577141454443336}, {'label': 'confusion', 'score': 0.0017739335307851434}, {'label': 'amusement', 'score': 0.0016857136506587267}, {'label': 'optimism', 'score': 0.001521028229035437}, {'label': 'fear', 'score': 0.001519678276963532}, {'label': 'love', 'score': 0.0010892795398831367}, {'label': 'curiosity', 'score': 0.001072304672561586}, {'label': 'surprise', 'score': 0.0009586639353074133}, {'label': 'gratitude', 'score': 0.0009402834111824632}, {'label': 'caring', 'score': 0.0009109770180657506}, {'label': 'desire', 'score': 0.0008522178395651281}, {'label': 'embarrassment', 'score': 0.0007042935467325151}, {'label': 'pride', 'score': 0.00045252524432726204}, {'label': 'relief', 'score': 0.00042013623169623315}, {'label': 'grief', 'score': 0.00039499395643360913}, {'label': 'nervousness', 'score': 0.00034457253059372306}, {'label': 'remorse', 'score': 0.0002891776675824076}]]
out[0].sort(key=lambda item: item["label"])
print(out[0])

vector = []
for a in out[0]:
    vector.append( a.get("score"))

print(vector)
