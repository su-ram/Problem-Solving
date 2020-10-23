import java.util.*;

public class Main {

    // 백준 7562. 나이트의 이동.

    static int length;
    static Position targetNode;
    static int [][] visited;

    static class Position{

        int x;
        int y;
        int path;

        Position(String[] node){
            this.x = Integer.parseInt(node[0]);
            this.y = Integer.parseInt(node[1]);
            this.path = 0;
        }

        Position(int x, int y){
            this.x = x;
            this.y = y;
            this.path = 0;

        }
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();

        scanner.nextLine();



        for(int i=0; i< num; i++){

            length = scanner.nextInt();
            visited = new int [length][length];
            scanner.nextLine();



            String[] start = scanner.nextLine().split(" ");
            String[] target = scanner.nextLine().split(" ");

            
            Position startNode = new Position(start);
            targetNode = new Position(target);

            BFS(startNode);





        }

    }

    public static void BFS(Position start){
        Queue<Position> queue = new LinkedList<Position>();
        queue.offer(start);
        int xx, yy;
        Position curPos, nextPos;

        int [] dx = {2,2,1,1};
        int [] dy = {1,-1,2,-2};


        while(!queue.isEmpty()){

            curPos = queue.poll();


            if (curPos.x == targetNode.x && curPos.y == targetNode.y){
                System.out.println(curPos.path);
                break;
            }

            if(visited[curPos.x][curPos.y] == 1){

                continue;
            }
            visited[curPos.x][curPos.y] = 1;

            for(int i=0; i<2; i++){
                for(int j=0; j<4; j++){
                     xx = curPos.x + dx[j];
                     yy = curPos.y + dy[j];


                     if(xx>=0 && xx < length && yy >= 0 && yy < length && visited[xx][yy] == 0){
                         nextPos = new Position(xx,yy);
                         nextPos.path = curPos.path+1;
                         queue.offer(nextPos);
                     }




                     dx[j] *= -1;
                     dy[j] *= -1;

                }
            }
        }

    }


}
