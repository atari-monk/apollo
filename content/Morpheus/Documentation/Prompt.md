# Prompts

## Table of Contents

- [Class Documentation Template](#class-documentation-template)
- [Scene Documentation Template](#scene-documentation-template)
- [Interface Group Documentation Template](#interface-group-documentation-template)
- [Module Documentation Template](#module-documentation-template)

# Class Documentation Template
[Back to Table of Contents](#table-of-contents)

1. Given this template in next prompt i will provide a class to document.

	````markdown
		# **Class Documentation Template**

		### **Class Name:** `YourClassName`

		---

		### **1. Class Purpose**
		- **Description:**
		Briefly explain the responsibility of the class.
		_Example: This class is responsible for managing the user authentication process, including login, logout, and session management._

		---

		### **2. Key Methods and Properties**
		- **Primary Methods:**
		- `methodName1(param1, param2)`
			- **Description:** Explain what the method does.
			- **Behavior:** Describe any non-obvious behavior or side effects.
			- **Returns:** Mention the return value.
			- **Exceptions:** List any exceptions or errors thrown.
		- `methodName2(param1)`
			- **Description:** Explain what the method does.
			- **Behavior:** Describe any non-obvious behavior or side effects.
			- **Returns:** Mention the return value.

		- **Key Properties:**
		- `propertyName1`
			- **Description:** What the property represents.
			- **Behavior:** Explain any special behavior or calculations that this property might have.
		- `propertyName2`
			- **Description:** What the property represents.

		---

		### **3. Usage Examples**
		- **Example 1:**
		Provide an example of how the class and its methods should be used in practice.

			```python
			instance = YourClassName(param1, param2)
			result = instance.methodName1(param1, param2)
			```

		- **Example 2 (Optional):**
		Provide a second example for more advanced use or edge cases.

			```python
			instance = YourClassName()
			instance.propertyName = value
			instance.methodName2(param1)
			```

		---

		### **4. Dependencies and Interactions**
		- **Dependencies:**
		- List any modules, classes, or third-party libraries that the class depends on.
			_Example: This class relies on the `SessionManager` class for session persistence._

		- **Interactions with Other Classes:**
		- Describe how this class interacts with other components in the system.

		---

		### **5. Limitations and Assumptions**
		- **Known Limitations:**
		- List any restrictions or limitations of the class.
			_Example: This class does not support concurrent access and must be used in a single-threaded environment._

		- **Assumptions:**
		- Mention any assumptions made by the class regarding the state, environment, or input data.
			_Example: It assumes that the user data has been pre-validated before being passed into the class._

		---

		### **6. Additional Notes (Optional)**
		- Any extra details or considerations worth mentioning, such as version compatibility, potential future improvements, etc.

		---

		//Given this template in next prompt i will provide a class to document.
	````

# Scene Documentation Template
[Back to Table of Contents](#table-of-contents)

2. Given this template in next prompt i will provide a scene description, fill template with it to produce documentation.

	```markdown
		### **Scene Name:** `YourSceneName`

		---

		### **1. Scene Overview**
		- **Description:**
		  Briefly describe the purpose and functionality of the scene.
		  _Example: This scene is designed to test the spriteRenderer system, handle sprite positioning, and demonstrate the use of sprite flipping._

		- **Version:** `1.0.0`
		  - Mention the version of the scene.

		---

		### **2. Key Features**
		- **Primary Elements:**
		  - List and explain the primary elements within the scene, such as sprites, objects, or UI components.

			- **Element 1: Player1**
			  - **Position:** `430, 540`
			  - **Description:** Rendered to show how spriteRenderer draws position from the top left of the sprite.
			- **Element 2: Player2**
			  - **Position:** _Defined via transform.position._
			  - **Description:** Rendered using the `sprite.spriteOffset` property to demonstrate sprite translation for centering.
			- **Element 3: Player3 and Player4**
			  - **Position:** `Player1 and Player2` flipped horizontally with an x+100 translation.
			  - **Description:** Used to test sprite flipping.

		- **Core System Components:**
		  - `spriteRenderer 1.0.0`
			- **Description:** Renders the transform position from the top-left corner of the sprite.
		  - `canvasScaler`
			- **Description:** Handles scaling for the scene.

		---

		### **3. Behavior and Logic**
		- **Special Behavior:**
		  - **spriteRenderer Positioning:** The system renders `transform.position` as the top-left point of the sprite in version 1.0.0.
		  - **sprite.spriteOffset:** Demonstrates how the spriteOffset property moves the sprite so that the transform.position is at the sprite's center.
		  
		- **Behavioral Notes:**
		  - Initial decisions, such as the use of `sprite.spriteOffset`, were made early in development and are now considered suboptimal. Kept for historical purposes.
		  
		---

		### **4. Usage and Configuration**
		- **How to Load the Scene:**
		  Provide instructions on how to configure and load this scene.

			```json
			"select": {
				"folder": "engine",
				"subFolder": "",
				"scene": "renderer100"
			}
			```

		---

		### **5. Dependencies and Interactions**
		- **Dependencies:**
		  - List any modules, systems, or third-party libraries required for the scene to function.
			_Example: Depends on the spriteRenderer system and canvasScaler._

		- **Interactions with Other Systems:**
		  - Describe how this scene interacts with other game systems, components, or scenes.

		---

		### **6. Limitations and Assumptions**
		- **Known Limitations:**
		  - Describe any issues or limitations in this scene.
			_Example: The sprite rendering method is inefficient due to the improper use of `sprite.spriteOffset`._
		  
		- **Assumptions:**
		  - Any assumptions made while designing the scene.
			_Example: Assumes that sprite flipping only affects horizontal orientation._

		---

		### **7. Historical Notes (Optional)**
		- **Reasoning for Deprecated/Legacy Features:**
		  - Explain why certain outdated features remain, even if they are no longer in use or optimal.
			_Example: Kept as a point of reference to show what not to do in future versions._

		---
		
		//Given this template in next prompt i will provide a scene description, fill template with it to produce documentation.
	```

# Interface Group Documentation Template
[Back to Table of Contents](#table-of-contents)

3. Given this template in next prompt i will provide a interface group, fill template with it to produce documentation.

	```markdown
		### **Interface Group Documentation Template**

		### **Interface Group Name:** `YourInterfaceGroupName`

		---

		### **1. Group Purpose**
		- **Description:**
		  Briefly describe the common purpose or theme of the interface group.
		  _Example: This group of interfaces is designed to standardize communication between various data storage mechanisms, including relational databases, NoSQL databases, and file-based systems._

		---

		### **2. Common Responsibilities Across Interfaces**
		- **Shared Purpose:**
		  - Describe any shared responsibilities or functionality that the interfaces provide across the group.
		  _Example: All interfaces in this group provide methods for CRUD operations (Create, Read, Update, Delete) on different types of data stores._

		---

		### **3. Key Interfaces and Their Methods**
		For each interface in the group, document the purpose and key methods.

		- **Interface Name:** `YourInterfaceName1`
		  - **Primary Methods:**
			- `methodName1(param1, param2)`
			  - **Description:** Explain what the method does.
			  - **Behavior:** Describe any non-obvious behavior or side effects.
			  - **Returns:** Mention the return value.
			  - **Exceptions:** List any exceptions or errors thrown.
			- `methodName2(param1)`
			  - **Description:** Explain what the method does.
			  - **Behavior:** Describe any non-obvious behavior or side effects.
			  - **Returns:** Mention the return value.

		- **Interface Name:** `YourInterfaceName2`
		  - **Primary Methods:**
			- `methodName1(param1)`
			  - **Description:** Explain what the method does.
			  - **Behavior:** Describe any non-obvious behavior or side effects.
			  - **Returns:** Mention the return value.

		---

		### **4. Usage Examples**
		- **Example 1 (Basic Implementation):**
		  Provide an example of how an interface from the group might be implemented in practice.

			```python
			class MyClass(YourInterfaceName1):
				def methodName1(self, param1, param2):
					# Implementation here
					pass
			```

		- **Example 2 (Advanced Usage or Multiple Interfaces):**
		  Show an example of using multiple interfaces together or implementing advanced features.

			```python
			class MyAdvancedClass(YourInterfaceName1, YourInterfaceName2):
				def methodName1(self, param1, param2):
					# Implementation here
					pass
				  
				def methodName2(self, param1):
					# Implementation here
					pass
			```

		---

		### **5. Dependencies and Interactions**
		- **Dependencies:**
		  - List any modules, other interfaces, or third-party libraries that these interfaces depend on.
			_Example: All interfaces in this group rely on the `Logger` utility for logging operations._

		- **Interactions with Other Interfaces or Classes:**
		  - Describe how these interfaces are expected to interact with other parts of the system or with each other.
			_Example: Interfaces in this group are often implemented by classes that interact with the `ServiceManager` for lifecycle management._

		---

		### **6. Variations and Extensibility**
		- **Known Variations:**
		  - List any significant variations between interfaces in the group, or ways they might be extended.
			_Example: `YourInterfaceName1` is designed for synchronous data access, while `YourInterfaceName2` supports asynchronous operations._

		- **Extensibility:**
		  - Mention how new interfaces can be added to this group or how existing interfaces can be extended.
			_Example: New interfaces should conform to the same basic method signature pattern but may add specialized methods for new storage types._

		---

		### **7. Limitations and Assumptions**
		- **Known Limitations:**
		  - List any restrictions or limitations of the interface group.
			_Example: Interfaces in this group do not provide methods for transaction management, which must be handled externally._

		- **Assumptions:**
		  - Mention any assumptions made by the interfaces regarding state, environment, or input data.
			_Example: It is assumed that all data passed into these interfaces has been pre-validated._

		---

		### **8. Additional Notes (Optional)**
		- Any extra details or considerations worth mentioning, such as implementation guidelines, version compatibility, potential future improvements, etc.
		  _Example: Future versions of this group may include interfaces that support distributed transactions._

		---
		//Given this template in next prompt i will provide a interface group, fill template with it to produce documentation.
	```

# Module Documentation Template
[Back to Table of Contents](#table-of-contents)

4. Given this template in next prompt i will provide a module with function group, fill template with it to produce documentation.

```markdown
		### **Module Documentation Template**

		### **Module Name:** `YourModuleName`

		---

		### **1. Module Purpose**
		- **Description:**
		  Briefly describe the purpose or functionality of the module.
		  _Example: This module provides utility functions for mathematical operations, including basic arithmetic, statistical calculations, and complex number manipulations._

		---

		### **2. Common Responsibilities**
		- **Shared Functionality:**
		  - Describe any common functionality that the functions within the module provide.
		  _Example: All functions in this module accept numerical input and return results based on mathematical principles._

		---

		### **3. Key Functions and Their Details**
		For each function in the module, document the purpose, parameters, and return values.

		- **Function Name:** `functionName1(param1, param2)`
		  - **Description:** Explain what the function does.
		  - **Parameters:**
			- `param1` (Type): Description of the parameter.
			- `param2` (Type): Description of the parameter.
		  - **Returns:** Describe the return value, including type.
		  - **Exceptions:** List any exceptions or errors that might be raised.
		  
		- **Function Name:** `functionName2(param1)`
		  - **Description:** Explain what the function does.
		  - **Parameters:**
			- `param1` (Type): Description of the parameter.
		  - **Returns:** Describe the return value, including type.
		  - **Exceptions:** List any exceptions or errors that might be raised.

		---

		### **4. Usage Examples**
		- **Example 1 (Basic Usage):**
		  Provide a simple example of how to use a function from the module.

			```python
			result = functionName1(10, 20)
			print(result)  # Expected output: 30
			```

		- **Example 2 (Advanced Usage):**
		  Show an example that demonstrates more complex usage or combinations of functions.

			```python
			def advanced_calculation():
				result1 = functionName1(5, 15)
				result2 = functionName2(result1)
				print(result2)  # Expected output based on function logic
			```

		---

		### **5. Dependencies and Interactions**
		- **Dependencies:**
		  - List any modules, libraries, or other dependencies required by this module.
			_Example: This module relies on the `math` module for advanced mathematical operations._

		- **Interactions with Other Modules:**
		  - Describe how this module interacts with other parts of the system or other modules.
			_Example: Functions in this module are often called by the `DataAnalyzer` module to perform calculations._

		---

		### **6. Variations and Extensibility**
		- **Known Variations:**
		  - Describe any significant variations between functions in the module or how they can be extended.
			_Example: Some functions may accept optional parameters for additional functionality, such as specifying a precision level._

		- **Extensibility:**
		  - Mention how new functions can be added to this module or how existing functions can be extended.
			_Example: New functions should follow the naming convention and parameter structure established in existing functions._

		---

		### **7. Limitations and Assumptions**
		- **Known Limitations:**
		  - List any limitations of the module or its functions.
			_Example: The functions do not handle non-numeric input gracefully and will raise a TypeError._

		- **Assumptions:**
		  - Mention any assumptions made by the functions regarding input data or environment.
			_Example: It is assumed that all input parameters are within acceptable ranges for mathematical operations._

		---

		### **8. Additional Notes (Optional)**
		- Any extra details or considerations worth mentioning, such as implementation guidelines, version compatibility, potential future improvements, etc.
		  _Example: Future updates may include additional functions for handling matrix operations._

		---
		//Given this template in next prompt i will provide a module with function group, fill template with it to produce documentation.
```