import java.util.*;

public class Main {

    static int num;
    static ArrayList<ArrayList<Integer>> adjList;

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        //그래프를 인접리스트로 표현.

        adjList = new ArrayList<>();
        num = scanner.nextInt();
        scanner.nextLine();
        ArrayList<Integer> ints;

        for(int i=0; i<num; i++){

            String[] input = scanner.nextLine().split(" ");
            ints = new ArrayList<Integer>();

            for(int j=0; j<num; j++){
                int index = Integer.parseInt(input[j]);
                if (index == 1){
                    ints.add(j);
                }
            }

            adjList.add(ints);


        }
        for(int i=0; i<num; i++){
            int [] result = BFS(i);
            for(int a : result){
                System.out.print(a+" ");
            }
            System.out.println();
        }

    }

    public static int [] BFS(int node){

        Queue<Integer> queue = new LinkedList<Integer>();
        int [] visited = new int[num];


        ArrayList<Integer> neighbor = adjList.get(node);
        int nextnode;

        for(int i=0; i< neighbor.size(); i++){
            queue.add(neighbor.get(i));
        }

        while(!queue.isEmpty()){


            nextnode = queue.poll();


            visited[nextnode] = 1;
            neighbor = adjList.get(nextnode);

            for(int x : neighbor){

                if (visited[x] == 0){
                    queue.add(x);
                }
            }
        }

        return visited;
    }
}
