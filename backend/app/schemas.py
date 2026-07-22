from pydantic import BaseModel

#user and auth

class UserCreate(BaseModel):
    name : str
    email : str
    password : str
    
class UserLogin(BaseModel):
    email : str
    password : str
    
class UserResponse(BaseModel):
    id : int 
    name : str
    email : str
    
    class config:
        from_attributes = True

class Token(BaseModel):
    access_token : str
    token_type : str


#product

class ProductCreate(BaseModel):
    name : str
    brand : str
    category : str
    price : float
    rating : float
    ram : int
    storage : int
    battery : int
    weight : float

class ProductResponse(BaseModel):
    id : int 
    class config:
        from_attributes = True

#comparison

class ComparisonCreate(BaseModel):
    titlle : str

class ComparisonResponse(BaseModel):
    id : int 
    title : str
    user_id : int 
    
    class config:
        from_attributes = True
    
class ComparisonProductCreate(BaseModel):
    comparison_id : int 
    product_id : int
    