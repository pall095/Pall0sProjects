

class  Employee():
    
    employee_list = []
    
    def __init__( self , name, id , salary, dep = "None" ):
        
        self.__id = id
        self.__name = name
        self.__salary = salary 
        self.__dep = dep
        Employee.employee_list.append( self )
        
        
    def __repr__( self ):
        
        return f"Employee: ( Id ={self.id}, Name ={self.name } , Salary ={self.salary } , Department = {self.dep } )"
    

    def calculate_salary( self , hours_worked ):
    
        if hours_worked > 50:
            
            overtime = abs( 50 - hours_worked )
            overtimeAmount = (overtime * ( self.salary / 50 ) )
            
            return self.salary + overtimeAmount
        
        else:
            
            return self.salary 
    


    @property
    def name( self ):
        return self.__name
    
    @name.setter
    def name( self, newName ):
        self.__name = newName 
    
    @property
    def id( self ):
        return self.__id
    
    @property
    def salary( self ):
        return self.__salary
    
    @property
    def dep( self ):
        return self.__dep
    
    @dep.setter
    def dep( self , newDep ):
        
        self.__dep = newDep 

    
    