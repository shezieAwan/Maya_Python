'''
	Script Name: Matte Shader
	Creation Data: 25/MAR/2019
	Created by : Shehzad Taj Awan, shehzi.awan@gmail.com

	Description: 6 different colors to be applied as Matte Shader via whole Obj Sel or face(s) selction 
'''

## IMPORT ##
import maya.cmds as cmds

##-----------------------##

## getting Color Code for Creating new ShdGrp 
def rsa_CodeName_Chk(*args):
	#either make new or skip, return SG full Name.
	codeName= args[0]
	r = args[1] ## r-> red
	g = args[2] ## g-> green
	b = args[3] ## b-> blue
	
	# Getting all ShadingEngines in a List
	sg_List = cmds.ls(type='shadingEngine')
	sgRequired = 'RSA_'+codeName+'_MatteSG'
	
	if sgRequired in sg_List:
		print 'Exists'
	else:
		#create New RSA_MAtteSG
		shdName = 'RSA_'+codeName+'_Matte'
		print 'Creating New: {0}'.format(shdName)
		newShader = cmds.shadingNode('RedshiftArchitectural', name= shdName, asShader=True)
		cmds.sets(name = shdName+'SG',renderable=True, noSurfaceShader=True, empty=True)
		cmds.connectAttr((shdName+'.outColor'), (shdName+'SG.surfaceShader'))
		
		cmds.setAttr('%s.diffuse'%shdName, r,g,b, type='double3')
		cmds.setAttr('%s.diffuse_weight'%shdName, 1)
		cmds.setAttr('%s.reflectivity'%shdName, 0)
		cmds.setAttr('%s.additional_color'%shdName, r,g,b, type='double3')	#<<--- Dynamic Color Values as 'args'

	return sgRequired

def getSel_Obj_Faces():
	
	#return Sel Obj(s) name or Face(s) single Obj
	selList = cmds.ls(selection=True)
	return selList

def CodeName(*args):
	
	#get the selected Object/Faces, DEF()
	codeName = args[0]
	getSelection =  getSel_Obj_Faces()
		
	#Check for the RSA_Red_MatteSG existance
	sgName = rsa_CodeName_Chk(*args)
		
	#Apply SG to the selected Obj/Faces, DEF()
	cmds.sets(getSelection, e=True, forceElement=sgName)

##-->> Main UI 
def matteShade_GUI_shezie():

	##-->> Checking and Del win if exists
	if (cmds.window("MatteShadersWindow", exists=True)):
		cmds.deleteUI("MatteShadersWindow")
	
	##-->> Making 'MatteShadersWindow' win
	window = cmds.window( "MatteShadersWindow", title = "matteShaders")
	cmds.frameLayout( label="Matte Shaders", cll=False )
	form = cmds.formLayout(numberOfDivisions=100)

	# Creating Element Blue
	object = cmds.button( command="CodeName('Blue',0,0,1)", backgroundColor=(0,0.254902,0.6), label="Blue", w=68, h=34)
	cmds.formLayout( form, edit=True, attachForm=[( object, 'top', 72), ( object, 'left', 206)] )
	#=========================================
	# Creating Element Green
	object = cmds.button( command="CodeName('Green',0,1,0)", backgroundColor=(0,1,0), label="Green", w=68, h=34)
	cmds.formLayout( form, edit=True, attachForm=[( object, 'top', 73), ( object, 'left', 118)] )
	#=========================================
	# Creating Element yellowCode
	object = cmds.button( command="CodeName('Yellow',1,1,0)", backgroundColor=(1,1,0), label="yellow", w=68, h=34)
	cmds.formLayout( form, edit=True, attachForm=[( object, 'top', 123), ( object, 'left', 205)] )
	#=========================================
	# Creating Element Cyan
	object = cmds.button( command="CodeName('Cyan',0,1,1)", backgroundColor=(0,1,1), label="Cyan", w=68, h=34)
	cmds.formLayout( form, edit=True, attachForm=[( object, 'top', 122), ( object, 'left', 27)] )
	#=========================================
	# Creating Element magenta
	object = cmds.button( command="CodeName('Magenta',1,0,1)", backgroundColor=(1,0,1), label="Magenta", w=68, h=34)
	cmds.formLayout( form, edit=True, attachForm=[( object, 'top', 123), ( object, 'left', 118)] )
	#=========================================
	# Creating Element Red
	object = cmds.button( command="CodeName('Red',1,0,0)", backgroundColor=(1,0,0), label="Red", w=68, h=34)
	cmds.formLayout( form, edit=True, attachForm=[( object, 'top', 71), ( object, 'left', 26)] )
	#=========================================

	cmds.setParent( '..' )
	cmds.setParent( '..' )
	cmds.showWindow( window )
	cmds.window( "MatteShadersWindow", edit=True, widthHeight=(320.0, 320.0))
	
	
matteShade_GUI_shezie()