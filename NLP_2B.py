from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

texts = {
    "Original 1": """Today is our dragon boat festival, in our Chinese culture, to celebrate it with all safe and great in our lives. Hope you too, to enjoy it as my deepest wishes. Thank your message to show our words to the doctor, as his next contract checking, to all of us. I got this message to see the approved message. In fact, I have received the message from the professor, to show me, this, a couple of days ago. I am very appreciated the full support of the professor, for our Springer proceedings publication.""",
    "Pipeline1 1": "Today is our dragon boat festival, in our Chinese culture, to celebrate it with all safety and great in our lives. Hope you too, enjoy it as my deepest wishes. Thank you for your message to show our words to the doctor, as his next contract checking, to all of us. I got this message to see the approved message. In fact, I have received the message from the professor, to show me, this, a couple of days ago. I am very appreciated the full support of the professor, for our Springer proceedings publication.",
    "Pipeline2 1": "Today is our dragon boat festival, in our Chinese culture, to celebrate it with all safe and great in our lives. Hope you too, to enjoy it as my deepest wishes. Thank your message to show our words to the doctor, as his next contract checking, to all of us. I got this message to see the approved message. In fact, I have received the message from the professor, to show me, this, a couple of days ago. I am very appreciated the full support of the professor, for our Springer proceedings publication.",
    "Pipeline3 1": "Today is our dragon boat festival in Chinese culture, to celebrate it with all safe and great in our lives. Hope you too enjoy it as my deepest wishes. Thank your message to show our words to the doctor, as his next contract checking, to all of us. I got this message to see the approved message. In fact, I have received the message from the professor to show me, this, a couple of days ago. I am very grateful for the full support of the professor for our Springer proceedings publication.",
    "ChatGPT 1": "Today is the Dragon Boat Festival, an important celebration in Chinese culture. We observe this occasion wishing for safety and happiness in our lives. I hope you also enjoy the festival, as this is my sincere wish for you. Thank you for your message and for communicating our thoughts to the doctor in relation to his upcoming contract review. I have received the approved message a couple of days ago from the professor, who has provided valuable support. I am truly grateful for the professor’s continued assistance with our Springer proceedings publication.",

    "Original 2": """During our final discuss, I told him about the new submission — the one we were waiting since last autumn, but the updates was confusing as it not included the full feedback from reviewer or maybe editor? Anyway, I believe the team, although bit delay and less communication at recent days, they really tried best for paper and cooperation. We should be grateful, I mean all of us, for the acceptance and efforts until the Springer link came finally last week, I think. Also, kindly remind me please, if the doctor still plan for the acknowledgments section edit before he sending again. Because I didn’t see that part final yet, or maybe I missed, I apologize if so. Overall, let us make sure all are safe and celebrate the outcome with strong coffee and future targets""",
    "Pipeline1 2": "During our final discuss, I told him about the new submission — the one we were waiting for since last autumn, but the updates were confusing as it did not include the full feedback from reviewer or maybe editor. Anyway, I believe the team, although a bit delayed and less communication at recent days, really tried best for paper and cooperation. We should be grateful, I mean all of us, for the acceptance and efforts until the Springer link finally came last week, I think. Also, please remind me, if the doctor still plans for the acknowledgments section edit before he's sending again. Because I didn’t see that part final yet, or maybe I missed, I apologize if so. Overall, let us make sure all are safe and celebrate the outcome with strong coffee and future targets.",
    "Pipeline2 2": "During our final discuss, I told him about the new submission — the one we were waiting since last autumn, but the updates were confusing as it not included the full feedback from reviewer or maybe editor? Anyway, I believe the team, although a bit of delay and less communication at recent days, they really tried best for paper and cooperation. We should be grateful, I mean all of us, for the acceptance and efforts until the Springer link came finally last week, I think. Also, kindly remind me please, if the doctor still plans for the acknowledgments section edit before he's sending again. Because I didn’t see that part final yet, or maybe I missed, I apologize if so. Overall, let us make sure all are safe and celebrate the outcome with strong coffee and future targets.",
    "Pipeline3 2": "During our final discuss, I told him about the new submission — the one we were waiting since last autumn, but the updates were confusing as it not included the full feedback from the reviewer or maybe editor? Although a bit delay and less communication at recent days, I believe the team really tried best for paper and cooperation. We should be grateful, I mean all of us, for acceptance and efforts until the Springer link came finally last week, I think. Also, kindly remind me if the doctor still plans for the acknowledgments section edit before he's sending again. Because I didn't see that part final yet, or maybe I missed, I apologize if so. Overall, let us make sure all are safe and celebrate the outcome with strong coffee and future targets.",
    "ChatGPT 2": "During our final discussion, I informed him about the new submission—the one we have been waiting for since last autumn. However, the updates were confusing because they did not include the complete feedback from the reviewer or possibly the editor. In any case, I believe that, despite some recent delays and reduced communication, the team has done their best regarding the paper and our collaboration. We should all be grateful for the acceptance and the efforts made until the Springer link finally arrived last week. Additionally, please kindly remind me if the doctor still intends to edit the acknowledgments section before resubmitting. I have not yet seen the final version of that part, or perhaps I missed it—if so, I apologize. Overall, let us ensure everyone is well and celebrate this achievement together—with strong coffee and new goals for the future."
}


model = SentenceTransformer('all-MiniLM-L6-v2')

labels = list(texts.keys())
embeddings = model.encode(list(texts.values()))

import numpy as np

for i in range(2):  
    print(f"\n=== COSINE SIMILARITY TO ORIGINAL TEXT {i+1} ===")
    original_emb = embeddings[i*5]  
    for j in range(1, 5):
        sim = cosine_similarity([original_emb], [embeddings[i*5 + j]])[0][0]
        print(f"{labels[i*5 + j]} vs Original {i+1}: {sim:.3f}")

for i in range(2):
    subset = embeddings[i*5:(i+1)*5]
    pca = PCA(n_components=2)
    reduced = pca.fit_transform(subset)
    plt.figure()
    for idx, point in enumerate(reduced):
        plt.scatter(point[0], point[1], label=labels[i*5 + idx])
        plt.text(point[0], point[1], labels[i*5 + idx], fontsize=8)
    plt.title(f"PCA Visualization of Embeddings for Text {i+1}")
    plt.legend()
    plt.show()
