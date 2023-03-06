from .LoadingLog import LoadingLog
LoadingLog.Start("consoleLog.py")


class Debug:
    #region --------------------------------- MEMBERS
    enableConsole = False
    _currentDepth = 0
    _indentationStyle = "|\t"
    #endregion

    def Start(functionName:str=None):
        '''Indicates the start of a debugging chain for fast, auto indentation that doesn't rely on getting the stack size'''
        if Debug.enableConsole == True:
            if(functionName != None):
                Debug.Log("["+functionName+"]:")
            Debug._currentDepth = Debug._currentDepth + 1
        pass

    def End():
        '''Closes an indentation when debugging. Put this at the end of debugged functions, along with a start at the top'''
        if Debug.enableConsole == True and Debug._currentDepth > 0:
            indentation = ""

            Debug._currentDepth = Debug._currentDepth - 1
            if Debug._currentDepth > 0:
                for x in range(0, Debug._currentDepth):
                    indentation = indentation + Debug._indentationStyle
            print(indentation + "-")
        pass

    def End(functionName:str=None):
        '''Closes an indentation when debugging. Put this at the end of debugged functions, along with a start at the top'''
        if Debug.enableConsole == True and Debug._currentDepth > 0:
            indentation = ""

            Debug._currentDepth = Debug._currentDepth - 1
            if Debug._currentDepth > 0:
                for x in range(0, Debug._currentDepth):
                    indentation = indentation + Debug._indentationStyle
            if(functionName != None):
                print(indentation + f"-{functionName}-")
            else:
                print(indentation + "-")
        pass

    def Log(logged:str):
        if Debug.enableConsole:
            #Calculate and create indentations
            indentation = ""
            if Debug._currentDepth > 0:
                for x in range(0, Debug._currentDepth):
                    indentation = indentation + Debug._indentationStyle

            print(indentation + str(logged))
        pass

    def Warn(logged:str):
        if Debug.enableConsole:
            #Calculate and create indentations
            indentation = ""
            if Debug._currentDepth > 0:
                for x in range(0, Debug._currentDepth):
                    indentation = indentation + Debug._indentationStyle

            print(indentation + "[WARNING]:\t" + logged)
        pass

    def Error(logged:str):
        if Debug.enableConsole:
            #Calculate and create indentations
            indentation = ""
            if Debug._currentDepth > 0:
                for x in range(0, Debug._currentDepth):
                    indentation = indentation + Debug._indentationStyle

            print(indentation + "[ERROR]:\t" + logged)
        pass

LoadingLog.End("consoleLog.py")