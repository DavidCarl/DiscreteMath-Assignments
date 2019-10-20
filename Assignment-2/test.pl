class(class-1,1,monday).
class(class-2,2,monday).
class(class-3,1,tuesday).
class(class-4,1,wednesday).
class(class-5,2,wednesday).

studies(david,class-1).
studies(tjalfe,class-2).
studies(kasper,class-1).
studies(david,class-3).
studies(tjalfe,class-3).
studies(kasper,class-3).
studies(Alexander,class-4).
studies(david,class-5).
studies(Alexander,class-5).

has(S,D,C) :-
  class(C,Y,D),
  studies(S,C).