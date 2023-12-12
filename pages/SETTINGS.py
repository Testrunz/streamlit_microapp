import streamlit as st
st.header('DOE')
st.subheader('For generating table')
st.write("Generate a full design of experiment matrix in a table for a _________(coffee baking) example. Factors = 2, __________(fractional factorial design), level 2, Resolution is 5. Update the table with actual factor values instead of the coded +1 and -1.The actual values are oven _________(temp: 10,20, bakingtime: 5,10 each Taste,color) with empty values. Return the response in a json format having each factor and response has key and its respective values in a list and only return the dictionary.Return full table. Don't return the generated table, any asumption text or any other texts.")
st.subheader('For assuming reasonable values')
st.write("Assume reasonable value for the response variables based on the other features/inputs(values must be in range 0 to 10) and return the response in json format with each feature and response in separate key and its corresponsing values in a list. Don't return any unwanted text and any unicode text.")
st.header("FMEA")
st.write('generate full design FMEA for ______(ebike) in a table format and add atleast 3 failure modes for each of the item/function?. Only return the generated FMEA table and don"t return any unwanted texts.')
st.header("PROCESS MAP")
st.write('Generate graph map (mermaid code) for “________” cleaning a washing machine including output for each step . The output should be in between vertical slash and the input should be in between square brackets. The process should be ending with only a input and don"t include yes or no outputs or any questioning outputs or inputs. The graph map should be in sequence. Don"t return any numbers or any unwanted text, description of the response. Don"t return flowchart diagram')
st.header('SEQUENCE DIAGRAM')
st.write('Generate sequence diagram (mermaid code) for __________(making a coffee using a coffee maker). Don"t return any numbers or any unwanted text, description of the response. Don"t return flowchart diagram.')
st.header('TEST CASES')
st.subheader('Extracting headers')
st.write("Extract all the headers which is present at the start of new line and present only after a integer. Don't consider the text as heading if the integer which is present before the heading is not continuous and don't include its sub-headings. Don't include 'Scope','references','general requirements','test','annexes','TERMINOLOGY','instructions','purpose','Definitions','testing','instruments','Requirements' and other related words as headings. Return the response as dictionary with its respection clauses. Don't return any unwanted texts. Final answer should be in the following format: '''json {'text':[headings],'clause':[respective clauses]}'''. Ensure that all strings are enclosed in double quotes. Don't return any unwanted quotes like ``` json")
st.subheader("For extracting text present below the selected test cases:")
st.write('Extract text which is present below the title "{test_name}" keeping the format as it is in the context. For some headings text will be available from the contents page but don"t include those text available in the content page. If you can"t extract the answer or if you don"t the answer, just say we don"t have answer for this {test_name}, don"t try to make up an answer')