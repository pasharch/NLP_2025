from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

original_sent1 = "Thank your message to show our words to the doctor, as his next contract checking, to all of us."
reconstructed_sent1 = "Thank you for your message to show our words to the doctor, as his next contract review, to all of us."

original_sent2 = "During our final discuss, I told him about the new submission — the one we were waiting since last autumn, but the updates was confusing as it not included the full feedback from reviewer or maybe editor?"
reconstructed_sent2 = "During our final discussion, I told him about the new submission — the one we were waiting for since last autumn, but the updates were confusing as it did not include the full feedback from the reviewer or maybe editor?"

sentences = [
    original_sent1,
    reconstructed_sent1,
    original_sent2,
    reconstructed_sent2
]
labels = [
    "Original 1A",
    "Reconstructed 1A",
    "Original 2A",
    "Reconstructed 2A"
]

model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(sentences)

sim1 = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
sim2 = cosine_similarity([embeddings[2]], [embeddings[3]])[0][0]
print(f"Cosine similarity (Sentence 1): {sim1:.3f}")
print(f"Cosine similarity (Sentence 2): {sim2:.3f}")

pca = PCA(n_components=2)
reduced = pca.fit_transform(embeddings)
plt.figure(figsize=(6, 5))
for idx, point in enumerate(reduced):
    plt.scatter(point[0], point[1], label=labels[idx])
    plt.text(point[0]+0.01, point[1]+0.01, labels[idx], fontsize=10)
plt.legend()
plt.title("PCA Visualization of Sentence Embeddings (Παραδοτέο 1A)")
plt.show()
