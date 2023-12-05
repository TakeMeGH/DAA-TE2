import random

def generate_dataset(n, number_of_subset):
    # Menghasilkan himpunan universal U
    U = list(range(1, n + 1))

    # Menginisialisasi himpunan S dengan subset kosong
    S = [[] for _ in range(number_of_subset)]

    # Menjamin setiap elemen di U muncul di setidaknya satu subset di S
    for elem in U:
        S[random.randint(0, number_of_subset-1)].append(elem)

    # Menambahkan elemen tambahan secara acak ke setiap subset di S
    for subset in S:
        subset.extend(random.sample(U, random.randint(0, min(5, n-len(subset)))))

    # Menghilangkan duplikat dalam setiap subset
    S = [list(set(subset)) for subset in S]

    # Menghasilkan bobot untuk setiap subset di S
    P = [random.randint(1, 20) for _ in S]

    return len(U), S, P

if __name__=='__main__':
    # Menghasilkan dataset untuk 20, 200, dan 2000 elemen
    dataset_20 = generate_dataset(20)
    dataset_200 = generate_dataset(200)
    dataset_2000 = generate_dataset(2000)

    # Menampilkan hasilnya (opsional)
    print("Dataset untuk 20 elemen:", dataset_20)
    print("Dataset untuk 200 elemen:", dataset_200)
    print("Dataset untuk 2000 elemen:", dataset_2000)
