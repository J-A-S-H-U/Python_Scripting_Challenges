module seq_detector ( output logic detect, input logic in, clk, rst);

typedef enum {S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, C0, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, PRE_DEC, DEC, PRE_DL, DL, PRE_ISO, ISO} state;
state current, next;

always@(posedge clk or negedge rst)
if (!rst && current != DL)	current <= S0;
else		current <= next;

always_comb
casex (current)
	S0	:	if (!in) next = S0;					//detect 1
			else	next = C0;
			
	C0	:	if (!in) next = S0;									//check 1
			else	next = S1;
			
	S1	:	if (!in) next = C1;					//detect 0
			else 	next = C0;
			
	C1	:	if (!in) next = S2;									//check 0
			else	next = S1;
			
	S2	:	if 	(!in) next = C2;				//detect 0
			else	next = C0;
			
	C2	:	if (!in) next = S3;									//check 0
			else	next = S2;
			
	S3	:	if	(!in) next = PRE_DEC;				//detect 1
			else	next = C3;
	
	C3	:	if (!in) next = S3;									//check 1
			else	next = S4;
			
	S4	:	if (!in) next = C4;
			else	next = C0;					//detect 0
			
	C4	:	if (!in) next = S5;									//check 0
			else	next = S4;
			
	S5	:	if (!in) next = C5;					//detect 0
			else	next = C0;
			
	C5	:	if (!in) next = S6;									//check 0
			else	next = S5;
			
	S6	:	if (!in) next = S0;					//detect 1
			else	next = C6;
			
	C6	:	if (!in) next = S6;									//check 1
			else	next = S7;
			
	S7	:	if (!in) next = C4;					//detect 1
			else	next = C7;
			
	C7	:	if (!in) next = S7;									//check 1
			else	next = S8;
			
	S8	:	if (!in) next = C8;
			else	next = C0;					//detect 0
			
	C8	:	if (!in) next = S9;									//check 0
			else	next = S8;
			
	S9	:	if (!in) next = C9;					//detect 0
			else	next = C0;
			
	C9	:	if (!in) next = S10;								//check 0
			else	next = S9;
			
	S10	:	if (!in) next = S0;					//detect 1
			else	next = C10;
			
	C10	:	if (!in) next = S10;								//check 1
			else	next = S11;
			
	S11	:	if (!in) next = C4;					//detect 1
			else	next = C11;
			
	C11	:	if (!in) next = S11;								//check 1
			else	next = S12;
			
	S12	:	if (!in) next = C1;					//detect overlap
			else	next = C0;
			
	PRE_DEC	:	if (!in)	next = DEC;
			else	next = S3;
			
	DEC	:	if (!in)	next = PRE_ISO;
			else	next = PRE_DL;
			
	PRE_ISO	:	if(!in)	next = ISO;
				else	next = DEC;
	
	ISO	:	if (!rst)	next = S0;
			else	next = ISO;
			
	PRE_DL	:	if(!in)	next = DEC;
				else	next = DL;
			
	DL	:	next = DL;
	
endcase
	
	
always_comb
unique case(current)
	S12 :	detect = '1;
	
	default :	detect = '0;
	
endcase

`ifdef ASSERTIONS
assert property (@(posedge clk) !($isunknown(current)));
assert property (@(posedge clk) !($isunknown(detect)));
assert property (@(posedge clk) (!rst) |=> (current == S0));
assert property (@(posedge clk) (current == S0 && in == 1) |=> (current == C0 && detect == 0));
assert property (@(posedge clk) (current == S3 && in == 0) |=> (current == PRE_DEC && detect == 0));
assert property (@(posedge clk) (current == DEC && in == 0) |=> (current == PRE_ISO && detect == 0));
assert property (@(posedge clk) (current == DEC && in == 1) |=> (current == PRE_DL && detect == 0));
assert property (@(posedge clk) (current == DL && rst == 0) |=> (current == DL && detect == 0));
assert property (@(posedge clk) (current == DL && !($isunknown(in))) |=> (current == DL && detect == 0));
assert property (@(posedge clk) (current == ISO && rst && !($isunknown(in))) |=> (current == ISO && detect == 0));
assert property (@(posedge clk) (current == ISO && !rst) |=> (current == S0 && detect == 0));
assert property (@(posedge clk) (current == C11 && in == 1) |=> (current == S12 && detect == 1));
assert property (@(posedge clk) (current == S12) |-> (detect == 1));
assert property (@(posedge clk) (current == S12 && in == 1) |=> (current == C0));
assert property (@(posedge clk) (current == S12 && in == 0) |=> (current == C1));

`endif

endmodule