    '''
    专题推荐
    '''
    def get(self,request):

        subject = CmsSubject.objects.all()[0:1]
        subject_s = CmsSubjectModelSerializer(subject,many=True)
        mes = {}
        mes['code'] = 200
        mes['subject'] = subject_s.data
        return Response(mes)
