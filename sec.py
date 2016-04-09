File file = new File("F:\\A-small-practice.in");
File outFile = new File("F:\\A-small-practice.out");
BufferedReader br = new BufferedReader(new FileReader(file));
BufferedWriter bw = new BufferedWriter(new FileWriter(outFile));
int testCases = Integer.parseInt(br.readLine());
for(int t=1;t<=testCases;t++){
    print "hehe"

bw.write("Case #" + t +": Yes I did it\n");
}
br.close();
bw.close();
