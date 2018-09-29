
// Definition for singly-linked list.
public class ListNode {
  int val;
  ListNode next;
  ListNode(int x) { val = x; }
}
class OwnSolution {
  // O(n) = n+1
  // memeory complexity = O(2n)
  public ListNode middleNodeList(ListNode head) {
    ListNode pointer = head;
    LinkedList<ListNode> list = new LinkedList<>();
    while(pointer != null){
        list.add(pointer);
        pointer = pointer.next;
    }
    return list.get(list.size()%2==0?list.size()/2:(list.size()-1)/2);
  }
  // O(n) = n+1/2n
  // memory complexity = O(n)
  public ListNode middleNodeRevisit(ListNode head) {
    ListNode pointer = head;
    int counter = 0;
    while(pointer != null){
        counter++;
        pointer = pointer.next;
    }
    System.out.println(counter);
    if(counter %2 == 0){
        counter = counter / 2 +1;
    }
    else{
        counter = (counter+1)/2;
    }
    System.out.println(counter);
    ListNode pointerTwo = head;
    for(int i = 0;i<counter-1;i++){
        pointerTwo = pointerTwo.next;
    }
    return pointerTwo;
  }
}

class AnswerSolution{
  
}