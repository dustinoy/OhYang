# MergeSort VS HeapSort  

---

## 排序方式
- MergeSort

把原本的list切割為多等份，並兩個兩個比較，穩定性高。
- HeapSort

以二元樹的方式，不斷調換順序，找出序列中最大值和最小值，並上下互換抓出最大值，然後不斷的heapify直到排序完成，heapify的過程會因為序列本身的排列順序不同，複雜性也不同，所以為不穩定。
## 時間複雜度
- MergeSort

最好：Ο(n log n)                                            

最糟：Ο(n log n)

平均：Ο(n log n)

- HeapSort

最好：Ο(n log n)

最糟：Ο(n log n)

平均：Ο(n log n)

## 空間複雜度
- MergeSort

需要使用到2個以上的list來儲存結果

O(n)

- HeapSort

只有在原有的的二元樹調換數值的位置，但還有額外新增的儲存list

O(n)+O(1)

