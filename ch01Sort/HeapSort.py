# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/6/11'

# 堆排（完全二叉树：直接利用列表）
# （1）从最后一个非叶子节点开始，构建初始大根堆：根比孩子大
# （2）将第一个元素（最大）与最后一个元素交换，此时[0,...,n-1]为无序，[n]为有序，对[0,...,n-1]进行（1）
#      再将第一个元素与无序列表中最后一个交换,此时[0,...,n-2]无序,[n-1,n]有序，对[0,...,n-2]进行（2），以此类推

class HeapSort:
	'''堆排类'''
	def Max_Heapify(self, heap, heapsize, root):
		'''堆调整，使得根节点值大于子节点值'''
		left = root * 2 + 1  # 列表从0开始，左节点下标为 2i+1,右节点下标为 2i+2
		right = left + 1
		larger = root
		if left < heapsize and heap[left] > heap[larger]:
			larger = left
		if right < heapsize and heap[right] > heap[larger]:
			larger = right
		if larger != root:
			heap[larger], heap[root] = heap[root], heap[larger]
			self.Max_Heapify(heap, heapsize, larger)

	def Build_Max_Heap(self, heap):
		'''构建初始大根堆'''
		heapsize = len(heap)
		for i in range((heapsize-2)//2, -1, -1):
			# 从最后一个非叶子节点开始构建
			self.Max_Heapify(heap, heapsize, i)

	def Heap_Sort(self, heap):
		'''堆排序'''
		self.Build_Max_Heap(heap)
		for i in range(len(heap)-1, -1, -1):
			heap[0], heap[i] = heap[i], heap[0]
			self.Max_Heapify(heap, i, 0)
		return heap[::-1]

if __name__ == '__main__':
	heap = [30, 50, 57, 77, 62, 78, 94, 80, 84]
	hs = HeapSort()
	print("待排序大根堆：", end=' ')
	print(heap)
	print("大根堆排序  ：", end=' ')
	sort_heap = hs.Heap_Sort(heap)
	print(sort_heap)