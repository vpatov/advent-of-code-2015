import httplib2, subprocess, os
from bs4 import BeautifulSoup
import re


day_pattern = re.compile(r'---\s+.*\s+---')
http = httplib2.Http()
base_url = 'http://adventofcode.com/2015'
day_suffix = '/day/'

class template:
	cpp = """
	
void problem_main(){

}
	
int main(){
	std::cout<<"\\n";
	clock_t t1,t2;
    t1=clock();
	
	problem_main();
		
    t2=clock();
	cout<<"\\nProgram Execution Time: ";
    float diff ((float)t2-(float)t1);
	float seconds = diff / CLOCKS_PER_SEC;
    cout<<seconds<<" seconds."<<endl;
    return 0;

}
"""
	rust = """
extern crate time;
use time::PreciseTime;

fn problem_main(){

}

fn main() {
	let start_time = PreciseTime::now();
	
	problem_main();
	
	let end_time = PreciseTime::now();
	println!("\\nProgram Execution Time: {} seconds.\n",start_time.to(end_time));
}
"""
	python = """
import time
start_time = time.time()





total_time = time.time() - start_time
print "Program Execution Time:", total_time, "seconds."
"""
	java = """
	public static void main(String[]args){
		long start_time = System.currentTimeMillis();

		long end_time = System.currentTimeMillis();

	System.out.println("\\nProgram Execution Time: " + (end_time - start_time) + "seconds.");

	}

"""
def make_cpp_template(text,day):
	f = open('Problems/c++/day' + str(day) + '.cpp','w')
	f.write('/*\n' + text + '\n*/\n')
	f.write(template.cpp)
	f.close()
	 

def make_rust_template(text,day):
	p = subprocess.Popen("cargo new day" + str(day) + " --bin", shell=True,cwd=os.getcwd() + '/Problems/Rust')
	p.wait()
	f = open('Problems/rust/day' + str(day) +'/src/main.rs','w')
	f.write('/*\n' + text + '\n*/\n')
	f.write(template.rust)
	f.close()
	
def make_python_template(text,day):
	f = open('Problems/python/day' + str(day) + '.py','w')
	f.write('"""\n' + text + '\n"""\n')
	f.write(template.python)
	f.close()
	
def make_java_template(text,day):
	f = open('Problems/java/day' + str(day) + '.java','w')
	f.write('/*\n' + text + '\n*/\n')
	f.write('public class Day' + str(day) + '{\n')
	f.write(template.java)
	f.write('}')
	f.close()
	
	


for day in range(1,26):
	status,response = http.request(base_url + day_suffix + str(day))
	if (status['status'] != '200'):
		raise Exception("received a non-ok status")
	soup = BeautifulSoup(response,'lxml')
	article = soup.find('article',{'class':'day-desc'})
	desc = []
	for item in article.find_all():
		if item.name in ['em','span','code','a']:
			continue

		desc.append(item.text)
	for i in range(0,len(desc)):
		if day_pattern.search(desc[i]):
			desc[i] = desc[i] +'\n'
			break
	desc = ' '.join(desc)
	make_cpp_template(desc,day)
	make_python_template(desc,day)
	#make_rust_template(desc,day)
	make_java_template(desc,day)
	
	
	
	