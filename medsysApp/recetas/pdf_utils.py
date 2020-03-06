import os, io
from django.conf import settings
from django.http import FileResponse
from django.shortcuts import HttpResponse, get_object_or_404, render, HttpResponseRedirect, redirect
from django.urls import reverse, reverse_lazy
#Imports for Reportlab
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle, TA_CENTER, TA_LEFT
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image,BaseDocTemplate, Frame, PageTemplate, Paragraph
from functools import partial


def get_styles_customs(custom_style):
    
    styles = getSampleStyleSheet() 
    
    if custom_style == 'Titulo_C':
        
        Style_heading1_Center = ParagraphStyle('titulo1_centrado', 
                           alignment = TA_CENTER,
                        #    fontSize = 10,
                        #    fontName="Helvetica",
                           parent=styles['Heading1'],)
        return Style_heading1_Center

    if custom_style == 'Titulo_I':
        
        Style_heading1_Center = ParagraphStyle('titulo1_left', 
                           alignment = TA_LEFT,
                        #    fontSize = 10,
                        #    fontName="Helvetica",
                           parent=styles['Heading1'],)
        return Style_heading1_Center


    if custom_style == 'Titulo2_C':
        
        Style_heading2_Center = ParagraphStyle('titulo2_centrado', 
                           alignment = TA_CENTER,
                           parent=styles['Heading2'],)
        return Style_heading2_Center
    
    if custom_style == 'Titulo2_I':
        
        Style_heading2_Left = ParagraphStyle('titulo2_left', 
                           alignment = TA_LEFT,
                           parent=styles['Heading2'],)
        return Style_heading2_Left

    if custom_style == 'Normal_C':
        Style_normal_Center = ParagraphStyle('normal_centrado', 
                            alignment = TA_CENTER,
                            fontSize = 14,
                            leading = 28,
                            spacebefore=60,
                            spaceAfter=14,
                            parent=styles['Normal'],)
    
        return Style_normal_Center

    if custom_style == 'Normal_I':
        Style_normal_Left = ParagraphStyle('normal_left', 
                           alignment = TA_LEFT,
                            fontSize = 14,
                            leading = 28,
                            spacebefore=40,
                            spaceAfter=14,
                        #    fontName="Helvetica",
                           parent=styles['Normal'],)
    
        return Style_normal_Left

    if custom_style == 'Footer_C':
        Style_footer_Center = ParagraphStyle('parrafos', 
                           alignment = TA_CENTER,
                           fontSize = 10,
                           fontName="Helvetica")
        return Style_footer_Center

    else:
        Style_selected = styles['Normal']

    return Style_selected

def init_pdf_doc():
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Receta_view.pdf"'
    #for download 
    # response['Content-Disposition'] = 'attachment; filename="My Users.pdf"'
    #Se define el bufer 
    buff = io.BytesIO()
   
    return response, buff

def gen_pdf(request, template=None):
    h_orientacion = 'Titulo_'+template.header_id.orientacion
    f_orientacion ='Footer_'+template.orientacion
    response, buff  = init_pdf_doc()
    doc = SimpleDocTemplate(buff,pagesize=letter,rightMargin=40,leftMargin=40,topMargin=60,bottomMargin=18,)
    t=[]
    #cambiar el path a relativo - se usa full path para desarrollo
    #path relativo 
    # archivo_imagen2 = settings.MEDIA_ROOT+'/header/logo/login.png'
    #full path
    header = Paragraph(template.header_id.header, get_styles_customs(h_orientacion)) 
    logo = settings.MEDIA_ROOT+'/'+str(template.header_id.logo)
    imagen = Image(logo, width=50, height=50,hAlign='RIGHT')
    t.append(imagen)
    t.append(header)

    t.append(Paragraph('Rp./', get_styles_customs('Titulo2_I')))
    legend = request.POST.get('descripcion')
    content = str(legend).replace('\n','<br />\n')
   
    t.append(Paragraph(content, get_styles_customs('Normal_C')))

    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height,id='normal')
    header_content = Paragraph(template.footer_id.footer, get_styles_customs(f_orientacion))
    template = PageTemplate(id='test', frames=frame, onPage=partial(header_footer, content=header_content))
    doc.addPageTemplates([template])
    
    doc.build(t)  
    response.write(buff.getvalue())  
    buff.close()  
    
    return response  

def preview_template_asPDF(request,template=None):
    h_orientacion = 'Titulo_'+template.header_id.orientacion
    print('Orientacion Header', h_orientacion)
    f_orientacion ='Footer_'+template.footer_id.orientacion
    print('Orientacion Footer', f_orientacion)

    response, buff  = init_pdf_doc()
    doc = SimpleDocTemplate(buff,pagesize=letter,rightMargin=40,leftMargin=40,topMargin=60,bottomMargin=18,)
    t=[]
    header = Paragraph(template.header_id.header, get_styles_customs(h_orientacion)) 
    logo = settings.MEDIA_ROOT+'/'+str(template.header_id.logo)
    imagen = Image(logo, width=50, height=50,hAlign='RIGHT')
    t.append(imagen)
    t.append(header)
    t.append(Paragraph('Rp./', get_styles_customs('Titulo2_I')))
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height,id='normal')
    header_content = Paragraph(template.footer_id.footer, get_styles_customs(f_orientacion))
    template = PageTemplate(id='test', frames=frame, onPage=partial(header_footer, content=header_content))
    doc.addPageTemplates([template])

    doc.build(t)
    response.write(buff.getvalue())  
    buff.close()  
    return response  
    
def header_footer(canvas, doc, content):
        # Save the state of our canvas so we can draw on it
        canvas.saveState()
        # Header
        # header = Paragraph('This is a multi-line header.  It goes on every page.   ' * 5, styles['Normal'])
        # w, h = header.wrap(doc.width, doc.topMargin)
        # header.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin - h)
        # for f in template:
        #     Texto_footer=f.footer_id.footer
            
        # Footer
        # Texto_footer = """Dr. Carlos M. Rott |
        #     Especialista en Pediatria MP:1214 <br></br>Carlos Pellegrini 1780 |
        #     Tel.4427128 | Cel. 154540897 | carlosmrott@yahoo.com |
        #     W 3400 BBF - Corrientes - Argentina <br></br> 
        #     NO OLVIDE ESTA RECETA EN SU PROXIMA CONSULTA """
        #Armar el Texto para el Footer con el Estilo definido en get_styles_custom
        # footer = Paragraph(Texto_footer, get_styles_customs('Footer_Center'))   

        #Obtener el Ancho y ponerlo en W y en el H ponemos el margen inferior(bottonMargin) 
        w, h = content.wrap(doc.width, doc.bottomMargin)
        
        #dibujamos el footer sobre el canvas pasandole el margen izquierdo y el margen inferior
        content.drawOn(canvas, doc.leftMargin, h)
 
        # Release the canvas
        canvas.restoreState()

def view_receta_stored(request,receta):
    h_orientacion = 'Titulo_'+receta.template_id.header_id.orientacion
    f_orientacion ='Footer_'+receta.template_id.orientacion
    response, buff  = init_pdf_doc()
    doc = SimpleDocTemplate(buff,pagesize=letter,rightMargin=40,leftMargin=40,topMargin=60,bottomMargin=18,)
    t=[]
    #cambiar el path a relativo - se usa full path para desarrollo
    #path relativo 
    # archivo_imagen2 = settings.MEDIA_ROOT+'/header/logo/login.png'
    #full path
    header = Paragraph(receta.template_id.header_id.header, get_styles_customs(h_orientacion)) 
    logo = settings.MEDIA_ROOT+'/'+str(receta.template_id.header_id.logo)
    imagen = Image(logo, width=50, height=50,hAlign='RIGHT')
    t.append(imagen)
    t.append(header)
   
    t.append(Paragraph('Rp./', get_styles_customs('Titulo2_L')))
    legend = receta.descripcion
    content = str(legend).replace('\n','<br />\n')
   
    t.append(Paragraph(content, get_styles_customs('Normal_C')))

       
    #definicion del footer
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height,id='normal')
    header_content = Paragraph(receta.template_id.footer_id.footer, get_styles_customs(f_orientacion))
    template = PageTemplate(id='test', frames=frame, onPage=partial(header_footer, content=header_content))
    doc.addPageTemplates([template])
    
    doc.build(t)  
    response.write(buff.getvalue())  
    buff.close()  
    
    return response  