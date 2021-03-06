t = ['bool', 'signed char', 'unsigned char', 'short', 'unsigned short', 
     'int', 'unsigned int', 'long', 'unsigned long', 'float', 'double', 
     'long double', 'long long', 'unsigned long long']

pt = '''template <>
struct PromoteTraits<%(A)s, %(B)s> : public detail::PromoteType<%(A)s, %(B)s>
{
    typedef detail::PromoteType<%(A)s, %(B)s>::Promote Promote;
    using detail::PromoteType<%(A)s, %(B)s>::toPromote;
};
'''

def ifdefAround(k, l, s):
    if (k in ['long long', 'unsigned long long']) or (l in ['long long', 'unsigned long long']):
        return '#ifdef LLONG_MAX\n'+s+'#endif // LLONG_MAX\n\n'
    else:
        return s + '\n'   

s = '''/************************************************************************/
/*                                                                      */
/*               Copyright 1998-2008 by Ullrich Koethe                  */
/*       Cognitive Systems Group, University of Hamburg, Germany        */
/*                                                                      */
/*    This file is part of the VIGRA computer vision library.           */
/*    The VIGRA Website is                                              */
/*        http://kogs-www.informatik.uni-hamburg.de/~koethe/vigra/      */
/*    Please direct questions, bug reports, and contributions to        */
/*        ullrich.koethe@iwr.uni-heidelberg.de    or                    */
/*        vigra@informatik.uni-hamburg.de                               */
/*                                                                      */
/*    Permission is hereby granted, free of charge, to any person       */
/*    obtaining a copy of this software and associated documentation    */
/*    files (the "Software"), to deal in the Software without           */
/*    restriction, including without limitation the rights to use,      */
/*    copy, modify, merge, publish, distribute, sublicense, and/or      */
/*    sell copies of the Software, and to permit persons to whom the    */
/*    Software is furnished to do so, subject to the following          */
/*    conditions:                                                       */
/*                                                                      */
/*    The above copyright notice and this permission notice shall be    */
/*    included in all copies or substantial portions of the             */
/*    Software.                                                         */
/*                                                                      */
/*    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND    */
/*    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES   */
/*    OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND          */
/*    NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT       */
/*    HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,      */
/*    WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING      */
/*    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR     */
/*    OTHER DEALINGS IN THE SOFTWARE.                                   */                
/*                                                                      */
/************************************************************************/
 
 
#ifndef VIGRA_PROMOTETRAITS_HXX
#define VIGRA_PROMOTETRAITS_HXX

// this file was autogenerated from promote_traits.hxx.py - DO NOT EDIT

'''
for k in t:
    s += ifdefAround(k, k, pt % { 'A': k, 'B': k})
    for l in t:
        if l == k: continue
        s += ifdefAround(k, l, pt % { 'A': k, 'B': l})

s += '''

#endif // VIGRA_PROMOTETRAITS_HXX
'''
open('promote_traits.hxx', 'w').write(s)

        
