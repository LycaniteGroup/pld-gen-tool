!!! note "Diagram"

	```mermaid
	flowchart TD
		classDef inprogress fill:#0c7dba;
		subgraph Legende
			InProgress[En cours ce sprint]:::inprogress 
		end
	```
	```mermaid
	flowchart TD
		classDef inprogress fill:#0c7dba;

		Lycanite[Lycanite]:::inprogress --> Website[Website]:::inprogress
		Lycanite --> Solution[Solution]:::inprogress
		Website --> Front[Frontend]
		Website --> Back[Backend]
		Solution --> Application[Application]:::inprogress
		Solution --> VFS[Virtual File System]
		Solution --> Service[Service]
		Solution --> KernelDriver[Kernel Driver]:::inprogress
	```

!!! tip "Features Progression Status"
	**Website**

	| Feature                          | Progress   |
	| -------------------------------- | ---------- |
	| Landing page mockup              | [=0% "0%"] |
	| FAQ page mockup                  | [=0% "0%"] |
	| Download page mockup             | [=0% "0%"] |
	| Contact page mockup              | [=0% "0%"] |
	| Website technologies             | [=0% "0%"] |
	| Development of the landing page  | [=0% "0%"] |
	| Development of the download page | [=0% "0%"] |
	| Development of the FAQ page      | [=0% "0%"] |
	| Development of the contact page  | [=0% "0%"] |

	<br>

	**Driver**

	| Feature                   | Progress     |
	| ------------------------- | ------------ |
	| Stack Library             | [=0% "0%"]   |
	| Queue Library             | [=0% "0%"]   |
	| Vector Library            | [=27% "27%"] |
	| Memory management library | [=0% "0%"]   |

	<br>

	**Application**

	| Feature                        | Progress   |
	| ------------------------------ | ---------- |
	| Mockup of the Application      | [=0% "0%"] |
	| Application Architecture       | [=0% "0%"] |
	| Mockup of the Application - UX | [=0% "0%"] |
	| Application Technology         | [=0% "0%"] |

	<br>

	**Tools**

	| Feature                             | Progress   |
	| ----------------------------------- | ---------- |
	| Convert github issues/cards to text | [=0% "0%"] |
	| PDF Generation tool                 | [=0% "0%"] |

<br>

#### Website

!!! info "[Landing page mockup](https://github.com/LycaniteGroup/LycaniteWebsite/issues/3)"
	| As         | I want                       |
	| :--------- | :--------------------------- |
	| developper | a mockup of the landing page |

	| Description                                                                                                                      |
	| :------------------------------------------------------------------------------------------------------------------------------- |
	| Have a mockup of the landing page that suits the entire group so we have a streamlined view of what the website should look like |

	| Working Day(s) | Working People(s) |
	| :------------: | :---------------: |
	| 2              | 1                 |

	**Definition of Done**

	- [ ] A basic mockup of the landing page

	[=0% "0%"]

!!! info "[FAQ page mockup](https://github.com/LycaniteGroup/LycaniteWebsite/issues/4)"
	| As         | I want                   |
	| :--------- | :----------------------- |
	| developper | a mockup of the FAQ page |

	| Description                                                                                                                  |
	| :--------------------------------------------------------------------------------------------------------------------------- |
	| Have a mockup of the FAQ page that suits the entire group so we have a streamlined view of what the website should look like |

	| Working Day(s) | Working People(s) |
	| :------------: | :---------------: |
	| 2              | 1                 |

	**Definition of Done**

	- [ ] A basic mockup of the FAQ page

	[=0% "0%"]

!!! info "[Download page mockup](https://github.com/LycaniteGroup/LycaniteWebsite/issues/5)"
	| As         | I want                        |
	| :--------- | :---------------------------- |
	| developper | a mockup of the download page |

	| Description                                                                                                                       |
	| :-------------------------------------------------------------------------------------------------------------------------------- |
	| Have a mockup of the download page that suits the entire group so we have a streamlined view of what the website should look like |

	| Working Day(s) | Working People(s) |
	| :------------: | :---------------: |
	| 2              | 1                 |

	**Definition of Done**

	- [ ] A basic mockup of the download page

	[=0% "0%"]

!!! info "[Contact page mockup](https://github.com/LycaniteGroup/LycaniteWebsite/issues/6)"
	| As         | I want                       |
	| :--------- | :--------------------------- |
	| developper | a mockup of the contact page |

	| Description                                                                                                                      |
	| :------------------------------------------------------------------------------------------------------------------------------- |
	| Have a mockup of the contact page that suits the entire group so we have a streamlined view of what the website should look like |

	| Working Day(s) | Working People(s) |
	| :------------: | :---------------: |
	| 2              | 1                 |

	**Definition of Done**

	- [ ] A basic mockup of the contact page

	[=0% "0%"]

!!! info "[Website technologies](https://github.com/LycaniteGroup/LycaniteWebsite/issues/7)"
	| As             | I want                                                        |
	| :------------- | :------------------------------------------------------------ |
	| web developper | a global view of all of the web technologies available to use |

	| Description                                                                                                                                                                              |
	| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
	| Before starting development on the website, we need to choose technologies adapted to our needs based on their features. Keep in mind, the website is just a showcase one and not an app |

	| Working Day(s) | Working People(s) |
	| :------------: | :---------------: |
	| 2              | 3                 |

	**Definition of Done**

	- [ ] Look for different technologies
	- [ ] Test the different technologies
	- [ ] Getting used to them

	[=0% "0%"]

!!! info "[Development of the landing page](https://github.com/LycaniteGroup/LycaniteWebsite/issues/8)"
	| As         | I want                      |
	| :--------- | :-------------------------- |
	| developper | to program the landing page |

	| Description                                          |
	| :--------------------------------------------------- |
	| Development of the landing page based on it's mockup |

	| Working Day(s) | Working People(s) |
	| :------------: | :---------------: |
	| 2              | 1                 |

	**Definition of Done**

	- [ ] Development of the landing page

	[=0% "0%"]

!!! info "[Development of the download page](https://github.com/LycaniteGroup/LycaniteWebsite/issues/9)"
	| As         | I want                       |
	| :--------- | :--------------------------- |
	| developper | to program the download page |

	| Description                                           |
	| :---------------------------------------------------- |
	| Development of the download page based on it's mockup |

	| Working Day(s) | Working People(s) |
	| :------------: | :---------------: |
	| 2              | 1                 |

	**Definition of Done**

	- [ ] Development of the download page

	[=0% "0%"]

!!! info "[Development of the FAQ page](https://github.com/LycaniteGroup/LycaniteWebsite/issues/10)"
	| As         | I want                  |
	| :--------- | :---------------------- |
	| developper | to program the FAQ page |

	| Description                                      |
	| :----------------------------------------------- |
	| Development of the FAQ page based on it's mockup |

	| Working Day(s) | Working People(s) |
	| :------------: | :---------------: |
	| 2              | 1                 |

	**Definition of Done**

	- [ ] Development of the FAQ page

	[=0% "0%"]

!!! info "[Development of the contact page](https://github.com/LycaniteGroup/LycaniteWebsite/issues/11)"
	| As         | I want                      |
	| :--------- | :-------------------------- |
	| developper | to program the contact page |

	| Description                                          |
	| :--------------------------------------------------- |
	| Development of the contact page based on it's mockup |

	| Working Day(s) | Working People(s) |
	| :------------: | :---------------: |
	| 2              | 1                 |

	**Definition of Done**

	- [ ] Development of the contact page

	[=0% "0%"]

<br>

#### Driver

!!! info "[Stack Library](https://github.com/LycaniteGroup/LycaniteDriver/issues/3)"
	| As                 | I want                            |
	| :----------------- | :-------------------------------- |
	| Lycanite Developer | Have a Stack library ready to use |

	| Description                                                                                                                                                                                                                                                                                                                                            |
	| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
	| A stack is an abstract data type that serves as a collection of elements, with two main principal operations:<br><br>   - Push, which adds an element to the collection, and<br>   - Pop, which removes the most recently added element that was not yet removed.<br><br>We have to recreate a new stack because there is none natively in the kernel. |

	| Working Day(s) | Working People(s) |
	| :------------: | :---------------: |
	| 10             | 1                 |

	**Definition of Done**

	- [ ] Insert element at the beginning
	- [ ] Take out the first element
	- [ ] Sort the Stack
	- [ ] Automatic expansion before overflow
	- [ ] Memory Efficient and Safe
	- [ ] Works in the Kernel
	- [ ] Be able to reserve the size of a Stack
	- [ ] Documentation
	- [ ] Tests

	[=0% "0%"]

!!! info "[Queue Library](https://github.com/LycaniteGroup/LycaniteDriver/issues/4)"
	| As                 | I want                            |
	| :----------------- | :-------------------------------- |
	| Lycanite Developer | Have a Queue library ready to use |

	| Description                                                                                                                                                                     |
	| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
	| A queue is a data structure in which elements are removed in the same order they were entered.<br>We have to recreate a new queue because there is none natively in the kernel. |

	| Working Day(s) | Working People(s) |
	| :------------: | :---------------: |
	| 10             | 1                 |

	**Definition of Done**

	- [ ] Inserting elements at the end
	- [ ] Take out the first element
	- [ ] Sorted the Tail
	- [ ] Automatic enlargement before overflow
	- [ ] Memory Efficient and Safe
	- [ ] Works in the Kernel
	- [ ] Be able to reserve the size of a Queue
	- [ ] Documentation
	- [ ] Tests

	[=0% "0%"]

!!! info "[Vector Library](https://github.com/LycaniteGroup/LycaniteDriver/issues/2)"
	| As                 | I want                            |
	| :----------------- | :-------------------------------- |
	| Lycanite Developer | Have a Queue library ready to use |

	| Description                                                                    |
	| :----------------------------------------------------------------------------- |
	| We have to recreate a new vector because there is none natively in the kernel. |

	| Working Day(s) | Working People(s) |
	| :------------: | :---------------: |
	| 10             | 1                 |

	**Definition of Done**

	- [x] Inserting elements
	- [ ] Deleting elements
	- [x] Access to an element from an index
	- [ ] Vector sorting
	- [x] Automatic enlargement before overflow
	- [ ] Ability to reserve the size of a Vector
	- [ ] Memory Efficient and Safe
	- [ ] Binary search
	- [ ] Works in the Kernel
	- [ ] Documentation
	- [ ] Tests

	[=27% "27%"]

!!! info "[Memory management library](https://github.com/LycaniteGroup/LycaniteDriver/issues/1)"
	| As                 | I want                                                                             |
	| :----------------- | :--------------------------------------------------------------------------------- |
	| Lycanite developer | a cross-platform memory management library that allows me to manage memory easily. |

	| Description                                                                                                                |
	| :------------------------------------------------------------------------------------------------------------------------- |
	| We need to have a cross platform memory management library in order to easily manage the memory on the kernel driver side. |

	| Working Day(s) | Working People(s) |
	| :------------: | :---------------: |
	| 6              | 1                 |

	**Definition of Done**

	- [ ] Allocations, frees
	- [ ] Reallocations
	- [ ] Memory copies
	- [ ] Memory moves
	- [ ] Memory monitoring
	- [ ] Tests

	[=0% "0%"]

<br>

#### Application

!!! info "[Mockup of the Application](https://github.com/LycaniteGroup/LycaniteApplication/issues/1)"
	| As                  | I want                                               |
	| :------------------ | :--------------------------------------------------- |
	| Lycanite Developper | A model of the application to facilitate development |

	| Description                                                                                                                              |
	| :--------------------------------------------------------------------------------------------------------------------------------------- |
	| This model must be as User Friendly as possible to make its use simple and fast without disturbing the user. It will allow a faster use. |

	| Working Day(s) | Working People(s) |
	| :------------: | :---------------: |
	| 3              | 3                 |

	**Definition of Done**

	- [ ] Have the Lycanite color chart
	- [ ] Find a simple, smooth and interactive style with the chosen technology

	[=0% "0%"]

!!! info "[Application Architecture](https://github.com/LycaniteGroup/LycaniteApplication/issues/2)"
	| As                 | I want                                                                                                             |
	| :----------------- | :----------------------------------------------------------------------------------------------------------------- |
	| Lycanite Developer | Have an architecture allowing the creation of the application according to the model with the chosen technologies. |

	| Description                                                                                                                                                                                                                                                              |
	| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
	| Once the technology has been found, an architecture is needed to facilitate the development of the application so that, over time, it is easy to find its way around.<br>The architecture must allow the efficient implementation of new features not originally planned |

	| Working Day(s) | Working People(s) |
	| :------------: | :---------------: |
	| 10             | 3                 |

	**Definition of Done**

	- [ ] Take into account the needs of the technologies chosen for our architecture.
	- [ ] Creation of schematics and documentation detailing the architecture of the application and allowing other developers to understand its logic

	[=0% "0%"]

!!! info "[Mockup of the Application - UX](https://github.com/LycaniteGroup/LycaniteApplication/issues/3)"
	| As                  | I want                                               |
	| :------------------ | :--------------------------------------------------- |
	| Lycanite Developper | A model of the application to facilitate development |

	| Description                                                                                                                                             |
	| :------------------------------------------------------------------------------------------------------------------------------------------------------ |
	| This model must be as User Friendly as possible to make its use simple and fast without disturbing the user, for that, a good UX will be very important |

	| Working Day(s) | Working People(s) |
	| :------------: | :---------------: |
	| 9              | 3                 |

	**Definition of Done**

	- [ ] UX File permissions
	- [ ] UX Opening applications in Lycanite
	- [ ] UX Opening and writing permissions

	[=0% "0%"]

!!! info "[Application Technology ](https://github.com/LycaniteGroup/LycaniteApplication/issues/4)"
	| As                 | I want                                                                              |
	| :----------------- | :---------------------------------------------------------------------------------- |
	| Lycanite Developer | Have an overview of the different technologies available to develop the application |

	| Description                                                                                                                                                                                     |
	| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
	| To start the development of the Application from the mock-up in the most efficient way we need to be able to choose between the different existing technologies knowing their proposed features |

	| Working Day(s) | Working People(s) |
	| :------------: | :---------------: |
	| 6              | 3                 |

	**Definition of Done**

	- [ ] Research of existing technologies.
	- [ ] Testing the technologies to see if they allow us to achieve our objectives.
	- [ ] Acclimatisation to the technology

	[=0% "0%"]

<br>

#### Tools

!!! info "[Convert github issues/cards to text](https://github.com/LycaniteGroup/pld-gen-tool/issues/1)"
	| As                 | I want                                                           |
	| :----------------- | :--------------------------------------------------------------- |
	| Lycanite Developer | I want to generate text from github issues and cards I created | |

	| Description                                                                                                                              |
	| :--------------------------------------------------------------------------------------------------------------------------------------- |
	| I want to have a tool that converts github issues/cards into a text file format that can be easily understood and edited by team members |

	| Working Day(s) | Working People(s) |
	| :------------: | :---------------: |
	| 5              | 1                 |

	**Definition of Done**

	- [ ] Retrieve open and closed issues from github
	- [ ] Convert issues to proprietary text format

	[=0% "0%"]

!!! info "[PDF Generation tool](https://github.com/LycaniteGroup/pld-gen-tool/issues/2)"
	| As         | I want                                                     |
	| :--------- | :--------------------------------------------------------- |
	| Developper | A tool capable of generating a PDF file based on the PLD | |

	| Description                                              |
	| :------------------------------------------------------- |
	| A tool capable of reading a text and generate a PDF file |

	| Working Day(s) | Working People(s) |
	| :------------: | :---------------: |
	| 5              | 1                 |

	**Definition of Done**

	- [ ] Parse document and generate PDF

	[=0% "0%"]

<br>

