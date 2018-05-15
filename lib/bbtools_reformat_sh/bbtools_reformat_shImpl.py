# -*- coding: utf-8 -*-
#BEGIN_HEADER
#END_HEADER


class bbtools_reformat_sh:
    '''
    Module Name:
    bbtools_reformat_sh

    Module Description:
    A KBase module: bbtools_reformat_sh
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        #END_CONSTRUCTOR
        pass

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]


    def filter_contigs(self, ctx, params):
        """
        :param workspace_name: instance of String
        :param params: instance of type "ContigFilterParams" (Input
           parameters) -> structure: parameter "min_length" of Long,
           parameter "assembly_ref" of String
        :returns: instance of type "ContigFilterResults" (Output results) ->
           structure:
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN filter_contigs
        # print(params['min_length'], params['assembly_ref'])
        print(params['input_sequence_file'])
        returnVal = {}
        #END filter_contigs
        return [returnVal]