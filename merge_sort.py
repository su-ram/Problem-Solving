
def divide(divided_list:list) -> list:
    # 리스트의 원소 개수가 1이 될 때까지 리스트를 반으로 계속 나눕니다.
    # 반으로 나눈 왼쪽, 오른쪽 리스트를 병합합니다.

    if len(divided_list) ==1 :
        return divided_list

    mid = len(divided_list) // 2
    left = divide(divided_list[:mid])
    right = divide(divided_list[mid:])

    return merge(left, right)


def merge(left:list, right:list) -> list:
    # 두 개의 리스트를 오름차순으로 정렬하여 새로운 정렬된 리스트를 반환합니다.
    # 매개변수인 left, right 리스트는 이미 정렬된 리스트입니다.

    i, j = 0, 0
    sorted_list = []

    while i < len(left) and j < len(right):
        if left[i] < right[j] :
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    if i < len(left):
        sorted_list += left[i:]
    if j < len(right):
        sorted_list += right[j:]

    return sorted_list

arr = [685,283,728,594,836,828,553,701,700,899]
print(divide(arr))