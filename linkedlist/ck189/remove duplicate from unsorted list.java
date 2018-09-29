import java.util.Iterator;

class solution{
  /**
   * double loop algorithm
   * Time complexity: O(n^2)
   * Space complexity: O(1)
   * @param list list that need to remove duplicate element
   * @return new length of list
   * for each element in list
   * loop through all the element after
   * if find duplicate, remove it
   */
  public int doubleLoopSolution(LinkedList<Integer> list){
    for(int i=0;i<list.size();i++){
      for(int j=i+1;j<list.size();j++){
        if(list.get(i) == list.get(j)){
          list.remove(j);
        }
      }
    }
    return list.szie();
  }
  /**
   * set algorithm
   * Time complexity: O(n)
   * Space complexity: O(2)
   * @param list list that need to remove duplicate element
   * @return new length of list
   * for each element in list
   * add it to set, remove it from list
   * bacause set do not have duplicate element
   * get all different elements from set 
   * add to list again
   */
  public int setSolution(LinkedList<Integer> list){
    HashSet<Integer> set = new HashSet();
    for(int i=0;i<list.size();i++){
      set.put(list.get(i));
      list.remove(i);
    }
    Iterator<E> iterator = set.iterator();
    while(iterator.hasNext()){
      list.add(iterator.next());
    }
    return list.size();
  }
  /**
   * solution from leetcode 26
   * two pointer algoritm
   * Time complexity: O(n*log(n))
   * use of Collection.sort()
   * Space complexity: O(1)
   * @param list list that need to remove duplicate element
   * @return new length of list
   * loop through list
   * each time find a element different from original element
   * means the elements between i and k is same
   * so set next element to value of k 
   * and move i to the next
   */
  public int twoPointersolution(LinkedList<Integer> list){
    Collections.sort(list);
    int i =  0;
    for(int k=0;k<list.size();k++){
      if(list.get(k) != list.get(i)){
        i++;
        list.set(i,list.get(k));
      }
    }
    return i+1;
  }
}