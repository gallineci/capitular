export class Historia {
    public id: number;
    public titulo: string;
    public sinopse: string;
    public genero: number;
    public nome_genero: string;
    public estilo: number | null;
    public nome_estilo: string;
    public status: number;
    public nome_status: string;
    public autor: number;
    public foto: string | undefined;
    public criado_em: string;
  
    constructor() {
      this.id = 0;
      this.titulo = '';
      this.sinopse = '';
      this.genero = 0;
      this.nome_genero = '';
      this.estilo = null;
      this.nome_estilo = '';
      this.status = 1;
      this.nome_status = '';
      this.autor = 0;
      this.foto = '';
      this.criado_em = '';
    }
  }
  