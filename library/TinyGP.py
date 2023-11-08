import random
from Parameters import *
from copy import deepcopy


class TinyGP:
    def __init__(self, filename: str, seed: int | None):
        # fitness =  new double[POPSIZE];
        # seed = s;
        # if ( seed >= 0 )
        #     rd.setSeed(seed);
        # setup_fitness(fname);
        # for ( int i = 0; i < FSET_START; i ++ )
        #     x[i]= (maxrandom-minrandom)*rd.nextDouble()+minrandom;
        # pop = create_random_pop(POPSIZE, DEPTH, fitness );
        
        self.Parameters = self.read_problem(filename)
        self.Parameters.seed =seed

        fitness= []
        if seed >=0 :
            random.seed(seed)
        self.setup_fitness(filename)
        x=[]
        for i in range(FSET_START):
            x[i] = (self.Parameters.maxrandom - self.Parameters.minrandom) * random.random() + self.Parameters.minrandom
        pop = self.generate_random_programs(POPSIZE, DEPTH, self.Parameters.fitness)
        pass
    def generate_random_programs(self, n: int, max_depth:int, fitness:list[float]) -> list[str]:
            #     char [][]pop = new char[n][];
    #     int i;

    #     for ( i = 0; i < n; i ++ ) {
    #         pop[i] = create_random_indiv( depth );
    #         fitness[i] = fitness_function( pop[i] );
    #     }
    #     return( pop );
        pop=[]
        for i in range(0,n):
            pop[i]=self.generate_random_indiv(max_depth)
            fitness[i]=self.fitness_function(pop[i])
        return pop
    def fitness_function(Prog: str)->float:
        # int i = 0, len;
        # double result, fit = 0.0;

        # len = traverse( Prog, 0 );
        # for (i = 0; i < fitnesscases; i ++ ) {
        #     for (int j = 0; j < varnumber; j ++ )
        #         x[j] = targets[i][j];
        #     program = Prog;
        #     PC = 0;
        #     result = run();
        #     fit += Math.abs( result - targets[i][varnumber]);
        # }
        # return(-fit );
        fit =0.0
        x=[]
        len = self.traverse(Prog, 0)
        for i in range(0, self.Parameters.fitnesscases):
            for j in range(self.Parameters.varnumber):
                x[j]= self.Parameters.targets[i][j]
            program = Prog
            PC = 0 
            result = self.run()
            fit += abs(result - self.Parameters.targets[i][self.Parameters.varnumber])
        return -fit
    def run() -> float:
        # char primitive = program[PC++];
        # if ( primitive < FSET_START )
        #     return(x[primitive]);
        # switch ( primitive ) {
        #     case ADD : return( run() + run() );
        #     case SUB : return( run() - run() );
        #     case MUL : return( run() * run() );
        #     case DIV : {
        #                    double num = run(), den = run();
        #                    if ( Math.abs( den ) <= 0.001 )
        #                        return( num );
        #                    else
        #                        return( num / den );
        #                }
        # }
        # return( 0.0 ); // should never get here
        primitive = self.Parameters.program[self.Parameters.PC+1]
        if primitive < FSET_START:
            return x[primitive]
        if primitive ==ADD:
            return( self.run() + self.run() )
        elif primitive==SUB:
            return( self.run() - self.run() )
        elif primitive==MUL:
            return( self.run() * self.run() )
        elif primitive == DIV:
            num=self.run()
            den =self.run()
            if abs(den) <= 0.001:
                return num
            else:
                return num/den
        raise Exception("Should never get here!") 
        pass
    def setup_fitness():
        pass
    def generate_random_indiv(max_depth:int) -> list[chr]:
        # static char [] buffer = new char[MAX_LEN];
    
        # char [] ind;
        # int len;

        # len = grow( buffer, 0, MAX_LEN, depth );

        # while (len < 0 )
        #     len = grow( buffer, 0, MAX_LEN, depth );

        # ind = new char[len];

        # System.arraycopy(buffer, 0, ind, 0, len );
        # return( ind );

        buffer=[]
        ind=[]
        len=self.grow(buffer, 0, MAX_LEN, max_depth)

        while len < 0:
            len = self.grow(buffer, 0, MAX_LEN, max_depth)
        ind =deepcopy(buffer)
        return ind
    
    def grow(self, buffer: list[float], pos: int, max_len: int, depth: int) -> int:
        # char prim = (char) rd.nextInt(2);
        # int one_child;

        # if ( pos >= max )
        #     return( -1 );

        # if ( pos == 0 )
        #     prim = 1;

        # if ( prim == 0 || depth == 0 ) {
        #     prim = (char) rd.nextInt(varnumber + randomnumber);
        #     buffer[pos] = prim;
        #     return(pos+1);
        # }
        # else  {
        #     prim = (char) (rd.nextInt(FSET_END - FSET_START + 1) + FSET_START);
        #     switch(prim) {
        #         case ADD:
        #         case SUB:
        #         case MUL:
        #         case DIV:
        #             buffer[pos] = prim;
        #             one_child = grow( buffer, pos+1, max,depth-1);
        #             if ( one_child < 0 )
        #                 return( -1 );
        #             return( grow( buffer, one_child, max,depth-1 ) );
        #     }
        # }
        # return( 0 ); // should never get here
        prim=str(random.randint(2)) ###????????/
        if pos >=max_len:
            return -1
        if pos == 0:
            prim=1
        if prim==0 or depth==0:
            prim = str(random.randint(self.Parameters.varnumber + self.Parameters.randomnumber))
            buffer[pos]=prim
            return pos+1
        else:
            prim=str(random.randint(FSET_END - FSET_START +1) + FSET_START)
            if prim in [ADD, SUB, MUL, DIV]:
                buffer[pos] = prim
                one_child = self.grow(buffer, pos+1, max_len, depth-1)
                if one_child<0:
                    return -1
                return self.grow(buffer, one_child, max_len-1)
        raise Exception("run should never get here")

    def crossover(parent1: str, parent2=str ) -> list[chr]:
        # int xo1start, xo1end, xo2start, xo2end;
        # char [] offspring;
        # int len1 = traverse( parent1, 0 );
        # int len2 = traverse( parent2, 0 );
        # int lenoff;

        # xo1start =  rd.nextInt(len1);
        # xo1end = traverse( parent1, xo1start );

        # xo2start =  rd.nextInt(len2);
        # xo2end = traverse( parent2, xo2start );

        # lenoff = xo1start + (xo2end - xo2start) + (len1-xo1end);

        # offspring = new char[lenoff];

        # System.arraycopy( parent1, 0, offspring, 0, xo1start );
        # System.arraycopy( parent2, xo2start, offspring, xo1start,
        #         (xo2end - xo2start) );
        # System.arraycopy( parent1, xo1end, offspring,
        #         xo1start + (xo2end - xo2start),
        #         (len1-xo1end) );

        # return( offspring );

        offspring=[]
        len1=self.traverse(parent1, 0)
        len2=self.traverse(parent2, 0)

        xo1start= random.randint(len1)
        xo1end=self.traverse(parent1, xo1start)

        xo2start=random.randint(len2)
        xo2end=self.traverse(parent2,xo2start)

        lenoff=xo1start + (xo2end - xo2start) + (len1-xo1end)
        offspring.append(parent1[0:xo1start])

        offspring.append(parent2[xo2start:xo2end])

        offspring.append(parent1[xo1end:len1])

        return offspring
    
    def traverse(buffer:str, buffercount:int)->int:
        # if ( buffer[buffercount] < FSET_START )
        #     return( ++buffercount );

        # switch(buffer[buffercount]) {
        #     case ADD:
        #     case SUB:
        #     case MUL:
        #     case DIV:
        #         return( traverse( buffer, traverse( buffer, ++buffercount ) ) );
        # }
        # return( 0 ); // should never get here
        if buffer[buffercount] < FSET_START:
            buffercount+=1
            return buffercount
        if buffer in [ADD, SUB, MUL, DIV]:
            return self.traverse(buffer, self.traverse(buffer, buffercount+1))
        raise Exception("run should never get here")
    
    def mutation(parent: str, pmut: float)->list[chr]:
        # int len = traverse( parent, 0 ), i;
        # int mutsite;
        # char [] parentcopy = new char [len];

        # System.arraycopy( parent, 0, parentcopy, 0, len );
        # for (i = 0; i < len; i ++ ) {
        #     if ( rd.nextDouble() < pmut ) {
        #         mutsite =  i;
        #         if ( parentcopy[mutsite] < FSET_START )
        #             parentcopy[mutsite] = (char) rd.nextInt(varnumber+randomnumber);
        #         else
        #             switch(parentcopy[mutsite]) {
        #                 case ADD:
        #                 case SUB:
        #                 case MUL:
        #                 case DIV:
        #                     parentcopy[mutsite] =
        #                         (char) (rd.nextInt(FSET_END - FSET_START + 1)
        #                                 + FSET_START);
        #             }
        #     }
        # }
        # return( parentcopy );
        len=self.traverse(parent, 0)
        parentcopy=[]
        parentcopy=deepcopy(parent)
        for i in range(0,len):
            if random.random() < pmut:
                mutsite = i
                if parentcopy[mutsite] < FSET_START:
                    parentcopy[mutsite] = str(random.randint(self.Parameters.varnumber+self.Parameters.randomnumber))
                else:
                    if parentcopy[mutsite] in [ADD, SUB, MUL, DIV]:
                        parentcopy[mutsite]=str(random.randint(FSET_END - FSET_START + 1)) + FSET_START
        return parentcopy
    def evaluate(): ####### WĄTPLIWE
        # int gen = 0, indivs, offspring, parent1, parent2, parent;
        # double newfit;
        # char []newind;
        # print_parms();
        # stats( fitness, pop, 0 );
        # for ( gen = 1; gen < GENERATIONS; gen ++ ) {
        #     if (  fbestpop > -7) {
        #         System.out.print("PROBLEM SOLVED\n");
        #         System.exit( 0 );
        #     }
        #     for ( indivs = 0; indivs < POPSIZE; indivs ++ ) {
        #         if ( rd.nextDouble() < CROSSOVER_PROB  ) {
        #             parent1 = tournament( fitness, TSIZE );
        #             parent2 = tournament( fitness, TSIZE );
        #             newind = crossover( pop[parent1],pop[parent2] );
        #         }
        #         else {
        #             parent = tournament( fitness, TSIZE );
        #             newind = mutation( pop[parent], PMUT_PER_NODE );
        #         }
        #         newfit = fitness_function( newind );
        #         offspring = negative_tournament( fitness, TSIZE );
        #         pop[offspring] = newind;
        #         fitness[offspring] = newfit;
        #     }
        #     stats( fitness, pop, gen );
        # }
        # System.out.print("PROBLEM *NOT* SOLVED\n");
        # System.exit( 1 );



        stats(fitness, pop, 0) ######## CZY POTRZEBNE????????
        for gen in range(1, GENERATIONS):
            if fbest > -7:
                print("PROBLEM SOLVED")
                exit(0)
            for indiv in range(0, POPSIZE):
                if random.random()< CROSSOVER_PROB:
                    parent1 = self.tournament( self.Parameters.fitness, TSIZE )
                    parent2 = self.tournament( self.Parameters.fitness, TSIZE )
                    newind = self.crossover( self.Parameters.pop[parent1],self.Parameters.pop[parent2])
                else:
                    parent = self.tournament_selection(self.Parameters.fitness, TSIZE)
                    newind = self.mutation(self.Parameters.pop[parent], PMUT_PER_NODE )
                newfit = self.fitness_function( newind )
                offspring = self.negative_tournament( self.Parameters.fitness, TSIZE )
                self.Parameters.pop[offspring] = newind
                self.Parameters.fitness[offspring] = newfit
            stats( fitness, pop, gen )  ######## CZY POTRZEBNE????????
        print("PROBLEM *NOT* SOLVED\n")
        exit(1)
    def tournament_selection(fitness: list[float], tsize:int):
        # int best = rd.nextInt(POPSIZE), i, competitor;
        # double  fbest = -1.0e34;

        # for ( i = 0; i < tsize; i ++ ) {
        #     competitor = rd.nextInt(POPSIZE);
        #     if ( fitness[competitor] > fbest ) {
        #         fbest = fitness[competitor];
        #         best = competitor;
        #     }
        # }
        # return( best );
        best= random.randint(POPSIZE)
        fbest = -1.0e34
        for i in range(0, tsize):
            competitor = random.randint(POPSIZE)
            if fitness[competitor] > fbest:
                fbest=fitness[competitor]
                best = competitor
        return best
        pass
    def serialize():
        pass
    def deserialize():
        pass
