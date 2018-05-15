/*
A KBase module: bbtools_reformat_sh
*/

module bbtools_reformat_sh {
    /*
        Insert your typespec information here.
    */
    /* Input parameter types */
    typedef structure {
        string bbtools_reformat_sh;
        string input_sequence_file;        
    } BbtoolsReformatShParams;

    /* Output result types */
    typedef structure {
        string bbtools_reformat_sh;
        string output_sequence_file;
    } BbtoolsReformatShResults;
    
    funcdef bbtools_reformat_sh(BbtoolsReformatShParams params)
        returns (BbtoolsReformatShResults) authentication required;
};
