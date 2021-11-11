The Repository contains python code to convert a CSV file to JSON file to obtain a specific parent-child structure as required. Both the Beginner & the Intermediate Part has been implemented.

Project Organization:

├── README.md          <- The top-level README details & realted instructions.

├── input_data.csv     <- External data as provided

├── output_sample.json <- Output JSON file produced

├── Code.txt           <- The main code written in txt format

├── Unittest.txt       <- The testcase written in txt format

├── Dockerfile.txt     <- Docker file for dockerization

├── requirements.txt   <- The requirements file for generation of the required environment

├── csvtojson.py       <- The source code

└── test_csvtojson.py  <- The test case 



# Beginner Part

Python code has been prepared based on the sample file provided (data.csv)

Environment used: PyCharm IDE (Pycharm Community Edition 2021.1.1)
Libraries Used: a) pandas b) json

## Short description

The sample csv file (data.csv) given for case study has been loaded to a Pandas DataFrame. Then it was analyzed and empty cells were cleaned.
DataFrame is used here due to the ease of handling data in case of increase in the volume of data.(In my case I have renamed the given 'data.csv' file as 'input_data.csv')

In that later part dictionaries has been created to generate Parent-Child structure and finally it has been dumped into a json file.
The desired json file can be stored to the user's computer or it can be printed. Both options has been opted in the working solution.

For the entire solution, small functions were created for ease of understanding and unittesting of those functionalities as well.


### Providing input CSV file

The user needs to provide the path of the input file alongwith the name of the csv file as mentioned in the code as a comment.


### Getting Output File

The user needs to provide the desired path to store/save the output file alogwith the required name of the output json file as mentioned in the code as a comment.
The output file has been attached as 'output_sample.json'. Further the user can also obtain the file from the path given by the during execution of the program.

##### Notes on running the file

1) The code/ working solution has been provided in the file 'Code.md' attached in the mail.
2) The path of the source csv file and the output json should be provided by the user.
3) The Test case has been provided in a seperate file 'Unittest.md' attached in the mail.

###### Test Case

Test Cases were provided in a seperate file named : 'test_csvtojson.py' for unittesting. The user needs to put both (csvtojson.py & test_csvtojson.py) files in the same working directory in order to execute unittesting.


# Intermediate part

Dockerization has been done. Unittest has been implemented in the docker file also.


## Creating docker image

Step 1:  Copy the following attached files in the desired working directory to work with Docker.

         1) Dockerfile.txt 2) requirements.txt 3) csvtojson.py 4)test_csvtojson.py 5) input_data.csv (Renamed the input file (data.csv) as input_data.csv)

Step 2: Open the Power Shell in the working directory where the above required files have been copied.


Step 3:  Run the command to build the image- ( The Unittesting Results can be seen in the shell during creation of image)
         
         " docker build -t <desired image name> -f Dockerfile.txt ."


### Running Docker Container

Step1:  Run the command to run the container-

        " dcoker run -ti <image name provided by the user in the last step>"

#### Copy the produced output file from docker container to host computer

Step 1: Run the follwoing command to find the container ID and copy the same. 

        "docker ps -a" 

Step 2: Run the following command to copy the output file to the desired location or current working directory.

        "docker cp <ContainerID>:/usr/src/app/morssample.json <provide the path of the current working directory or the desired path"
        
        (Note: 'output_sample.json' is the name used in the program for the output file)


##### Mapping the docker container with current working directory of host computer

In order to store the output json file in the current working directory of the host computer, mapping is required. 
To map with, run the following command-

 " docker run -v <copy and put the path of the current working directory>:/usr/src/app <image name provided by the user in the first step>"

---------------------------------------------------------------------------------------------------------------------------------------------------











