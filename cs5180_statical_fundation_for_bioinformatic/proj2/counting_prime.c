#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

#define NHASH 263167 //Use a prime number!
#define MULT 31

#define MAX_WORD_LENGTH		15
#define MAX_NUMBER_OF_SEQUENCES 10
#define MAX_FILENAME_LENGTH	255
#define MAX_FILE_LENGTH 	500000

#define max(a,b) (((a) > (b)) ? (a) : (b))

struct node
{
	char *word;
	int total_count;
	int sequence_count;
	int last_matching_sequence_id; 
	struct node * next;
} node;

typedef enum {
        ASCENDING_TOTAL,
        ASCENDING_SEQUENCE,
        DESCENDING_TOTAL,
        DESCENDING_SEQUENCE,
        ASCENDING_WORDLENGTH,
        DESCENDING_WORDLENGTH
} sort_order_t;

sort_order_t sort_order = DESCENDING_TOTAL;
typedef struct node Node;
unsigned long total_number_words = 0;

Node *bin[NHASH];
Node** bin_array;

char input_sequences[MAX_NUMBER_OF_SEQUENCES][MAX_FILE_LENGTH];		
unsigned long sequence_lengths[MAX_NUMBER_OF_SEQUENCES];		

unsigned int hash(char *p)
{
	unsigned int h = 0;
	for(; *p; p++)
		h = MULT * h + *p;
	return h % NHASH;
}

void incword(char *s, int sequence_id)
{
	Node * p;
	int h = hash(s);
	for(p = bin[h]; p!= NULL; p = p->next)
	{
		if(strcmp(s, p->word) == 0)
		{
			p->total_count++;

        		if(sequence_id != p->last_matching_sequence_id)
	        	{
		                p->sequence_count++;
		                p->last_matching_sequence_id = sequence_id;
                        }

			return;
		}
	}

	p = (Node *)malloc(sizeof(node));
	if(!p)
		return;
	p->total_count = 1;
	p->sequence_count = 1;
	p->last_matching_sequence_id = sequence_id;
	p->word = (char *)malloc(strlen(s)+1);
	total_number_words++;
	strcpy(p->word, s);
	p->next = bin[h];
	bin[h] = p;
}




int compare( const void* ptr1, const void* ptr2)
{
        Node** np1, *(*np2);
        np1 = (Node**) ptr1;
        np2 = (Node**) ptr2;
        

        switch(sort_order) 
        {
            case ASCENDING_TOTAL:
                    if( (*np1)->total_count < (*np2)->total_count )
                            return -1;
                    if( (*np1)->total_count == (*np2)->total_count )
                            sort_order = ASCENDING_WORDLENGTH;                           
                    if( (*np1)->total_count > (*np2)->total_count )
                            return 1;
                    break;

            case ASCENDING_SEQUENCE:
                    if( (*np1)->sequence_count < (*np2)->sequence_count )
                            return -1;
                    if( (*np1)->sequence_count == (*np2)->sequence_count )
                            return 0;                           
                    if( (*np1)->sequence_count > (*np2)->sequence_count )
                            return 1;
                    break;

            case DESCENDING_TOTAL:
                    if( (*np1)->total_count > (*np2)->total_count )
                            return -1;
                    if( (*np1)->total_count == (*np2)->total_count )
                            return 0;                           
                    if( (*np1)->total_count < (*np2)->total_count )
                            return 1;
                    break;

            case DESCENDING_SEQUENCE:
                    if( (*np1)->sequence_count > (*np2)->sequence_count )
                            return -1;
                    if( (*np1)->sequence_count == (*np2)->sequence_count )
                            return 0;                           
                    if( (*np1)->sequence_count < (*np2)->sequence_count )
                            return 1;
                    break;

            case ASCENDING_WORDLENGTH:
                    if( strlen( (*np1)->word ) < strlen( (*np2)->word ))
                            return -1;
                    if( strlen( (*np1)->word ) == strlen( (*np2)->word ))
                            return 0;
                    if( strlen( (*np1)->word ) > strlen( (*np2)->word ))
                            return 1;
                    break;

            case DESCENDING_WORDLENGTH:
                    if( strlen( (*np1)->word ) > strlen( (*np2)->word ))
                            return -1;
                    if( strlen( (*np1)->word ) == strlen( (*np2)->word ))
                            return 0;
                    if( strlen( (*np1)->word ) < strlen( (*np2)->word ))
                            return 1;
                    break;                    
            default:
                    return 0;
                    break;
        }                    
}       

void sort_hash()
{
        Node* p;
        int i;
        unsigned long nwords = 0;
        
        bin_array = (Node**)malloc(total_number_words * (sizeof(Node*)));
        
        for(i = 0; i < NHASH; i++)
        {
                for(p = bin[i]; p!= NULL; p = p->next)
                {
                      bin_array[nwords++] = p; 
                }

        }         

        qsort(&bin_array[0], total_number_words, sizeof(Node*), compare);
                
}



void print_cmdline_error() {
	fprintf(stderr, "Error: improper command line arguments\n");
	fprintf(stderr, "Usage: word_count -min X -max Y [-descseq|-ascseq|-desctot|-asctot|-desclength|-asclength] filename [other filenames]\n");
	fprintf(stderr, "-min minimum word length\n");
	fprintf(stderr, "-max maximum word length\n");
	fprintf(stderr, "-descseq causes the output to be sorted in descending order of sequence counts\n");
	fprintf(stderr, "-ascseq  causes the output to be sorted in ascending order of sequence counts\n");
	fprintf(stderr, "-desctot causes the output to be sorted in descending order of total counts\n");
	fprintf(stderr, "-asctot  causes the output to be sorted in ascending order of total counts\n");
	fprintf(stderr, "-desclength causes the output to be sorted in descending order of word length\n");
	fprintf(stderr, "-asclength  causes the output to be sorted in ascending order of word length\n");	
	fprintf(stderr, "Example: word_count -min 3 -max 10 -asctot filename1 filename2 filname3\n");
	exit(1);
}


unsigned long open_copy(char* filename, char* cbuf)
{
	FILE *fp;
	fp = fopen(filename, "r");
	char next_char;
	unsigned long sequence_length = 0;
	
        if( fp == NULL)
        {
                fprintf(stderr, "Error: unable to open file %s\n", filename);
                exit(1);
        }	

        while( fgets(cbuf, MAX_FILE_LENGTH, fp) == NULL );
        
        fclose(fp) ;
        return strlen(cbuf);

}

int contain_num(char* seq, int len){
	for(int i=0; i<len; ++i)
		if(isdigit(seq[i]))
			return 1;
	return 0;
}

int main(int argc, char *argv[])
{
	int number_of_sequences = 0;
	int min_wordlength = 0;
	int max_wordlength = 0;

	int i,k;
	signed int j;
	
	if (argc == 1) { 
		print_cmdline_error();
	}

	for (i = 1; i < argc; i++) {
		if (strcmp(argv[i], "-min") == 0) {  // input file
			++i;  
			min_wordlength = atoi(argv[i]);

		} else if (strcmp(argv[i], "-asctot") == 0) {
			sort_order = ASCENDING_TOTAL;
		} else if (strcmp(argv[i], "-ascseq") == 0) {
                        sort_order = ASCENDING_SEQUENCE;
		} else if (strcmp(argv[i], "-desctot") == 0) {
			sort_order = DESCENDING_TOTAL;
		} else if (strcmp(argv[i], "-descseq") == 0) {
			sort_order = DESCENDING_SEQUENCE;
                } else if (strcmp(argv[i], "-asclength") == 0) {
			sort_order = ASCENDING_WORDLENGTH;
                } else if (strcmp(argv[i], "-desclength") == 0) {
			sort_order = DESCENDING_WORDLENGTH;
		} else if (strcmp(argv[i], "-max") == 0) {
			++i; 
			max_wordlength = atoi(argv[i]);
		} else {
			sequence_lengths[number_of_sequences] = open_copy(argv[i], &input_sequences[number_of_sequences][0]);
			++number_of_sequences;
		}
	}


	if( min_wordlength == 0 || max_wordlength == 0 || min_wordlength > max_wordlength )
	{
		fprintf(stderr, "Error: incorrect or missing minimum or maximum word length\n");
		exit(1);
	}

	if( number_of_sequences == 0)
	{
		fprintf(stderr, "Error: no input file names specified\n");
		exit(1);
	}

	fprintf(stderr,"min wordlength = %d\n", min_wordlength);
	fprintf(stderr,"max wordlength = %d\n", max_wordlength);
	fprintf(stderr,"number of input files = %d\n", number_of_sequences);

	char buf[MAX_WORD_LENGTH+1];
	int wl;

	// Enumeration
	for( i=0; i < number_of_sequences; i++)
	{
                for( wl = min_wordlength; wl < max_wordlength+1; wl++)               
                {
                        for( j=0; j < max( 0, (signed int)(sequence_lengths[i]-wl+1)); j++)
                        {
                                strncpy(buf, &input_sequences[i][j], wl);
                                if(contain_num(buf, wl))  continue;
                                buf[wl] = '\0';                         
                                incword(buf, i);
                        }
                }
	}
        
	// Sort the output
        sort_hash();

        printf("total number of words = %ld\n", total_number_words);

        for(i = 0; i < total_number_words; i++)
        {
                if( bin_array[i] == NULL )
                {
                        exit(1); 
                }

                printf("%-*s \t\t %d \t\t %d\n", max_wordlength, bin_array[i]->word, bin_array[i]->total_count, bin_array[i]->sequence_count);                             
        }

}
